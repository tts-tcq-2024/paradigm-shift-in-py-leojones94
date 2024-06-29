def is_Temperature_Ok(temperature):
    if temperature < 0 or temperature > 45:
        print("Temperature out of range!")
        return False
    return True

def is_Soc_Ok(soc):
    if soc < 20 or soc > 80:
        print("State of Charge out of range!")
        return False
    return True

def is_ChargeRate_Ok(chargeRate):
    if chargeRate > 0.8:
        print("Charge Rate out of range!")
        return False
    return True

def battery_Is_Ok(temperature, soc, chargeRate):
    return is_Temperature_Ok(temperature) and is_Soc_Ok(soc) and is_ChargeRate_Ok(chargeRate)

if __name__ == '__main__':
    assert battery_Is_Ok(25, 70, 0.7) == True
    assert battery_Is_Ok(50, 85, 0) == False
