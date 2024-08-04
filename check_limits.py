HIGH_TEMP_LIMIT = 45
LOW_TEMP_LIMIT = 0
LOW_TEMP_WARNING_LIMIT = 2.25
HIGH_TEMP_WARNING_LIMIT = 42.75
HIGH_SOC_LIMIT = 80
LOW_SOC_LIMIT = 20
LOW_SOC_WARNING_LIMIT = 24
HIGH_SOC_WARNING_LIMIT = 76
HIGH_CHARGERATE_WARNING_LIMIT = 0.76
HIGH_CHARGERATE_LIMIT = 0.8
parameter_dict = {'Temperature' : {
                            'PARAM_NAME' : 'Temperature',
                            LOW_TEMP_WARNING_LIMIT : 'LOW_Temperature_WARNING',
                            HIGH_TEMP_WARNING_LIMIT: 'HIGH_Temperature_WARNING',
                            },
                  'SOC' : {
                            'PARAM_NAME' : 'SOC',
                            LOW_SOC_WARNING_LIMIT: 'LOW_SOC_WARNING',
                            HIGH_SOC_WARNING_LIMIT: 'HIGH_SOC_WARNING',
                          },
                  'Charge Rate' : {
                            'PARAM_NAME' : 'Charge Rate',
                            HIGH_CHARGERATE_LIMIT: 'Charge Rate_Normal',
                            HIGH_CHARGERATE_WARNING_LIMIT: 'HIGH_Charge_Rate_WARNING',
                            
                          }
                  }
def parameter_range_selector(warn_name,warn_param):
    if parameter_dict[warn_param]['PARAM_NAME'] == warn_name:
      parameter_warning_limit = parameter_dict[warn_param]
      return parameter_warning_limit
    return None
    
def warning_level_selector(parameter_warning_limit,parameter_value):
  low_limit_value,low_warning_message = list(parameter_warning_limit.items())[1]
  high_limit_value,high_warning_message = list(parameter_warning_limit.items())[2]
  if parameter_value >= high_limit_value:
    return high_warning_message
  elif parameter_value <= low_limit_value:
    # print(low_warning_message)
    return low_warning_message

def warn_checker(param_val,warn_name,warn_param):
  if warn_param != None:
    parameter_limit = parameter_range_selector(warn_name,warn_param)
    if parameter_limit != None:
      warning_message = warning_level_selector(parameter_limit,param_val)
      print(warning_message)
      temp_warn_result = True
      return (temp_warn_result,warning_message)
  return True,(warn_name +"_Normal")

def temp_checker(temp,warn_param = None):
  t = range(0,45)
  if (temp not in t):
    temp_breach_message = "Temperature out of range"
    print (temp_breach_message)
    temp_result = False
    return temp_result,temp_breach_message
  temp_result, temp_message = warn_checker(temp,"Temperature",warn_param)
  return temp_result,temp_message
  
def soc_checker(soc,warn_param = None):
  s = range(20,80)
  if (soc not in s):
    soc_breach_message = "SOC out of range"
    print (soc_breach_message)
    soc_result = False
    return soc_result,soc_breach_message
  soc_result, soc_message = warn_checker(soc, "SOC", warn_param)
  return soc_result,soc_message
  
def charge_rate_checker(cr,warn_param = None):
  if cr > 0.8:
    cr_breach_message = "Charge Rate out of Range"
    print(cr_breach_message)
    cr_result = False
    return cr_result,cr_breach_message
  cr_result,cr_message = warn_checker(cr,"Charge Rate",warn_param)
  return cr_result,cr_message

def battery_is_ok(temperature, soc, charge_rate,warn_parameter=None):
  temp_result,temp_message = temp_checker(temperature,warn_parameter)
  soc_result,soc_message = soc_checker(soc,warn_parameter)
  cr_result,cr_message = charge_rate_checker(charge_rate,warn_parameter)
  message_list = [temp_message,soc_message,cr_message]
  battery_result = (temp_result and soc_result and cr_result)
  # print(message_list)
  return battery_result, message_list
  
import unittest

class TestParadigm(unittest.TestCase):
    
    def test_high_temp(self):
        self.assertEqual((battery_is_ok(44, 25, 0.7,'Temperature')),(True,['HIGH_Temperature_WARNING', 'SOC_Normal', 'Charge Rate_Normal']))
    
    def test_low_temp(self):
        self.assertEqual((battery_is_ok(1, 25, 0.7,'Temperature')),(True,['LOW_Temperature_WARNING', 'SOC_Normal', 'Charge Rate_Normal']))
    
    def test_high_soc(self):
        self.assertEqual((battery_is_ok(25, 77, 0.7,'SOC')),(True,['Temperature_Normal', 'HIGH_SOC_WARNING', 'Charge Rate_Normal']))
    
    def test_low_soc(self):
        self.assertEqual((battery_is_ok(25, 21, 0.7,'SOC')),(True,['Temperature_Normal', 'LOW_SOC_WARNING', 'Charge Rate_Normal']))

    def test_high_cr(self):
        self.assertEqual((battery_is_ok(30, 30, 0.78,'Charge Rate')),(True,['Temperature_Normal', 'SOC_Normal', 'HIGH_Charge_Rate_WARNING']))

    def test_low_cr(self):
        self.assertEqual((battery_is_ok(30, 30, 0,'Charge Rate')),(True,['Temperature_Normal', 'SOC_Normal', 'Charge Rate_Normal']))

    def test_out_of_range(self):
      self.assertEqual(battery_is_ok(50, 85, 0), (False,['Temperature out of range', 'SOC out of range', 'Charge Rate_Normal']))

if __name__ == '__main__':
  unittest.main()
