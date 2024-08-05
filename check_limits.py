import unittest

from battery_is_ok import battery_is_ok 

class TestParadigm(unittest.TestCase):
    
    def test_high_temp_warning(self):
        self.assertEqual((battery_is_ok(44, 25, 0.7,'Temperature')),(True,['HIGH_Temperature_WARNING', 'SOC_Normal', 'Charge Rate_Normal']))
    
    def test_low_temp_warning(self):
        self.assertEqual((battery_is_ok(1, 25, 0.7,'Temperature')),(True,['LOW_Temperature_WARNING', 'SOC_Normal', 'Charge Rate_Normal']))
    
    def test_high_soc_warning(self):
        self.assertEqual((battery_is_ok(25, 77, 0.7,'SOC')),(True,['Temperature_Normal', 'HIGH_SOC_WARNING', 'Charge Rate_Normal']))
    
    def test_low_soc_warning(self):
        self.assertEqual((battery_is_ok(25, 21, 0.7,'SOC')),(True,['Temperature_Normal', 'LOW_SOC_WARNING', 'Charge Rate_Normal']))

    def test_high_cr_warning(self):
        self.assertEqual((battery_is_ok(30, 30, 0.78,'Charge Rate')),(True,['Temperature_Normal', 'SOC_Normal', 'HIGH_Charge_Rate_WARNING']))

    def test_low_cr_warning(self):
        self.assertEqual((battery_is_ok(30, 30, 0,'Charge Rate')),(True,['Temperature_Normal', 'SOC_Normal', 'Charge Rate_Normal']))

    def test_out_of_range_breach(self):
      self.assertEqual(battery_is_ok(50, 85, 0), (False,['Temperature out of range', 'SOC out of range', 'Charge Rate_Normal']))

if __name__ == '__main__':
  unittest.main()
