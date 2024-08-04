from warning_check import warn_checker

def temp_checker(temp,warn_param = None):
  t = range(0,45)
  if (temp not in t):
    temp_breach_message = "Temperature out of range"
    print (temp_breach_message)
    temp_result = False
    return temp_result,temp_breach_message
  temp_result, temp_message = warn_checker(temp,"Temperature",warn_param)
  return temp_result,temp_message
