from warning_check import warn_checker

def charge_rate_checker(charge_rate,warn_param = None):
  if charge_rate > 0.8:
    charge_rate_breach_message = "Charge Rate out of Range"
    print(charge_rate_breach_message)
    charge_rate_result = False
    return charge_rate_result,charge_rate_breach_message
  charge_rate_result,charge_rate_breach_message = warn_checker(cr,"Charge Rate",warn_param)
  return charge_rate_result,charge_rate_breach_message
