def translate_to_common_units(value, parameter):
    return value

def map_breach_to_ranges(value, parameter):
    lower_limit = parameter['lower_limit']
    upper_limit = parameter['upper_limit']
    warning_tolerance = parameter['warning_tolerance']
    
    if value < lower_limit:
        return 'low_breach'
    elif value < lower_limit + (upper_limit * warning_tolerance):
        return 'low_warning'
    elif value > upper_limit:
        return 'high_breach'
    elif value > upper_limit - (upper_limit * warning_tolerance):
        return 'high_warning'
    else:
        return 'normal'

def translate_anomaly_to_message(anomaly, parameter):
    messages = {
        'low_breach': 'out of range',
        'low_warning': 'approaching low',
        'high_breach': 'out of range',
        'high_warning': 'approaching high'
    }
    return f"{parameter['name']} {messages[anomaly]}"

def check_parameter(value, parameter):
    anomaly = map_breach_to_ranges(value, parameter)
    message = translate_anomaly_to_message(anomaly, parameter)
    print(message)
    return anomaly != 'high_breach' and anomaly != 'low_breach'

def battery_is_ok(temperature, soc, charge_rate):
    parameters = [
        {'name': 'Temperature', 'lower_limit': 0, 'upper_limit': 45, 'warning_tolerance': 0.05},
        {'name': 'State of Charge', 'lower_limit': 20, 'upper_limit': 80, 'warning_tolerance': 0.05},
        {'name': 'Charge Rate', 'upper_limit': 0.8, 'warning_tolerance': 0.05}
    ]
    return all(check_parameter(value, parameter) for value, parameter in zip([temperature, soc, charge_rate], parameters))

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
