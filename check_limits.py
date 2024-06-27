def battery_is_ok(temperature, soc, charge_rate):
    error_messages = []
    
    if temperature < 0 or temperature > 45:
        error_messages.append('Temperature is out of range!')
    
    if soc < 20 or soc > 80:
        error_messages.append('State of Charge is out of range!')
    
    if charge_rate > 0.8:
        error_messages.append('Charge rate is out of range!')
    
    if error_messages:
        for error in error_messages:
            print(error)
        return False
    
    return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
