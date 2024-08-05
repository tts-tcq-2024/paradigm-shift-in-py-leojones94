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
    return low_warning_message
