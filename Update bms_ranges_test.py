import unittest
import bms_ranges_monitor

class test_battery_current_ranges(unittest.TestCase):
  def test_handled_failing_current_ranges(self):
    self.assertTrue(bms_ranges_monitor.current_ranges([]) == "Invalid Input")
    
  def test_passing_current_ranges(self):
    self.assertTrue(bms_ranges_monitor.current_ranges([3, 3, 4, 7 ,10, 11, 12, 13]) == "Valid Input") 
    
  def test_passing(self):
    self.assertTrue(bms_ranges_monitor.current_ranges([3, 3, 4, 7]) == "Valid Input") 

  def test_failing_current_ranges(self):
    self.assertTrue(bms_ranges_monitor.current_ranges([3,4,5,6,7,8]) == "Invalid Input")    #no continuous range,should give invalid
    

if __name__ == '__main__':
  unittest.main()
