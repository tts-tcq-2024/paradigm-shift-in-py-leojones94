from warning_check import warn_checker

def soc_checker(soc,warn_param = None):
  soc_result, soc_message = warn_checker(soc, "SOC", warn_param)
  soc_accepted_range = range(20,80)
  if (soc not in soc_accepted_range):
    soc_breach_message = "SOC out of range"
    print (soc_breach_message)
    soc_result = False
    return soc_result,soc_breach_message
  return soc_result,soc_message
