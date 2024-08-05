from warning_check import warn_checker

def temp_checker(temp,warn_param = None):
  temp_result, temp_message = warn_checker(temp,"Temperature",warn_param)
  temp_accepted_range = range(0,45)
  if (temp not in temp_accepted_range):
    temp_breach_message = "Temperature out of range"
    print (temp_breach_message)
    temp_result = False
    return temp_result,temp_breach_message
  return temp_result,temp_message
