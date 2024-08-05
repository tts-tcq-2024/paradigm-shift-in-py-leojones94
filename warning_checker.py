from parameter_range_checker import parameter_range_selector,warning_level_selector

def warn_checker(param_val,warn_name,warn_param):
  if warn_param != None:
    parameter_limit = parameter_range_selector(warn_name,warn_param)
    if parameter_limit != None:
      warning_message = warning_level_selector(parameter_limit,param_val)
      print(warning_message)
      temp_warn_result = True
      return (temp_warn_result,warning_message)
  return True,(warn_name +"_Normal")
