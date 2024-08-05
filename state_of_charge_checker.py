from warning_check import warn_checker

def soc_checker(soc,warn_param = None):
  s = range(20,80)
  if (soc not in s):
    soc_breach_message = "SOC out of range"
    print (soc_breach_message)
    soc_result = False
    return soc_result,soc_breach_message
  soc_result, soc_message = warn_checker(soc, "SOC", warn_param)
  return soc_result,soc_message
