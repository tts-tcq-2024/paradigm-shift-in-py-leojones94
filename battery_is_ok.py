from temperature_check import temp_checker
from state_of_charge_check import soc_checker
from charge_rate_check import charge_rate_checker

def battery_is_ok(temperature, soc, charge_rate,warn_parameter=None):
  temp_result,temp_message = temp_checker(temperature,warn_parameter)
  soc_result,soc_message = soc_checker(soc,warn_parameter)
  cr_result,cr_message = charge_rate_checker(charge_rate,warn_parameter)
  message_list = [temp_message,soc_message,cr_message]
  battery_result = (temp_result and soc_result and cr_result)
  return battery_result, message_list
