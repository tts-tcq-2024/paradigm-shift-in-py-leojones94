def temp_checker(temp):
  t = range(0,45)
  if (temp not in t):
    print ("Temperature out of range")
    return False
  return True

def soc_checker(soc):
  s = range(20,80)
  if (soc not in s):
    print ("State of Charge out of range")
    return False
  return True
  
def charge_rate_checker(cr):
  if cr > 0.8:
    print("Charge Rate out of range")
    return False
  return True

def battery_is_ok(temperature, soc, charge_rate):
  return (temp_checker and soc_checker and charge_rate_checker)

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
