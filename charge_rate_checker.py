from warning_check import warn_checker

def charge_rate_checker(cr,warn_param = None):
  if cr > 0.8:
    cr_breach_message = "Charge Rate out of Range"
    print(cr_breach_message)
    cr_result = False
    return cr_result,cr_breach_message
  cr_result,cr_message = warn_checker(cr,"Charge Rate",warn_param)
  return cr_result,cr_message
