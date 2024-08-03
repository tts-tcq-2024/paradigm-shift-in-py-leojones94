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
                            LOW_TEMP_WARNING_LIMIT : 'LOW_Temperature_WARNING',
                            HIGH_TEMP_WARNING_LIMIT: 'HIGH_Temperature_WARNING',
                            },
                  'SOC' : {
                            LOW_SOC_WARNING_LIMIT: 'LOW_SOC_WARNING',
                            HIGH_SOC_WARNING_LIMIT: 'HIGH_SOC_WARNING',
                          },
                  'Charge Rate' : {
                            HIGH_CHARGERATE_LIMIT: 'Normal',
                            HIGH_CHARGERATE_WARNING_LIMIT: 'HIGH_Charge_Rate_WARNING',
                            
                          }
                  }
def parameter_range_selector(parameter):
  for item in parameter_dict:
    if item == parameter:
      parameter_warning_limit = parameter_dict[item]
      return parameter_warning_limit
    
def warning_level_selector(parameter_warning_limit,parameter_value):
  low_limit_value,low_warning_message = list(parameter_warning_limit.items())[0]
  high_limit_value,high_warning_message = list(parameter_warning_limit.items())[1]
  print(low_limit_value)
  if parameter_value >= high_limit_value:
    return high_warning_message
  elif parameter_value <= low_limit_value:
    return low_warning_message

def temp_checker(temp,warn_param = None):
  t = range(0,45)
  if (temp not in t):
    print ("Temperature out of range")
    temp_result = False
    return temp_result
  temp_result = True
  if warn_param != None:
    parameter_limit = parameter_range_selector(warn_param)
    warning_message = warning_level_selector(parameter_limit,temp)
    temp_warn_result = (temp_result,warning_message)
    return temp_warn_result
  return temp_result
  
def soc_checker(soc, warn_param = None):
  s = range(20,80)
  if (soc not in s):
    print ("State of Charge out of range")
    soc_result = False
    return soc_result
  soc_result = True
  if warn_param != None:
    parameter_limit = parameter_range_selector('SOC')
    warning_message = warning_level_selector(parameter_limit,soc)
    soc_warn_result = (soc_result,warning_message)
    return soc_warn_result
  return soc_result
  
def charge_rate_checker(cr,warn_param = None):
  if cr > 0.8:
    print("Charge Rate out of Range")
    cr_result = False
    return cr_result
  cr_result = True
  if warn_param != None:
    parameter_limit = parameter_range_selector('Charge Rate')
    warning_message = warning_level_selector(parameter_limit,cr)
    cr_warn_result = (cr_result,warning_message)
    return cr_warn_result
  return cr_result

def battery_is_ok(temperature, soc, charge_rate,warn_parameter=None):
  if warn_parameter!=None:
    if warn_parameter == 'SOC':
      soc_result, warn_message = soc_checker(soc,warn_parameter)
      return ((temp_checker(temperature) and soc_result and charge_rate_checker(charge_rate)),warn_message)
    if warn_parameter == 'Temperature':
      temp_result,warn_message = temp_checker(temperature,warn_parameter)
      return ((temp_result and soc_checker(soc) and charge_rate_checker(charge_rate)),warn_message)
    if warn_parameter == 'Charge Rate':
      cr_result,warn_message = charge_rate_checker(charge_rate,warn_parameter)
      return ((temp_checker(temperature) and soc_checker(soc) and cr_result),warn_message)
  return ((temp_checker(temperature) and soc_checker(soc) and charge_rate_checker(charge_rate)))

import unittest

class TestParadigm(unittest.TestCase):
    
    def test_high_temp(self):
        self.assertEqual((battery_is_ok(44, 25, 0.7,'Temperature')),(True,'HIGH_Temperature_WARNING'))
    
    def test_low_temp(self):
        self.assertEqual((battery_is_ok(1, 25, 0.7,'Temperature')),(True,'LOW_Temperature_WARNING'))
    
    def test_high_soc(self):
        self.assertEqual((battery_is_ok(25, 77, 0.7,'SOC')),(True,'HIGH_SOC_WARNING'))
    
    def test_low_soc(self):
        self.assertEqual((battery_is_ok(25, 21, 0.7,'SOC')),(True,'LOW_SOC_WARNING'))

    def test_high_cr(self):
        self.assertEqual((battery_is_ok(30, 30, 0.78,'Charge Rate')),(True,'HIGH_Charge_Rate_WARNING'))

    def test_low_cr(self):
        self.assertEqual((battery_is_ok(30, 30, 0,'Charge Rate')),(True,'Normal'))

    def test_out_of_range(self):
      self.assertEqual(battery_is_ok(50, 85, 0), False)

    

if __name__ == '__main__':
  unittest.main()
