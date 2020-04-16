import unittest
from setup_and_teardown import *

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man=AiRobo("mega man",battery=50)
        
    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery,100)
        
    def test_say_name(self):
        self.assertEqual(
             self.mega_man.say_name(),
            "i am a MEGA MAN")
        
        self.assertEqual(self.mega_man.battery,49)
        
if __name__=="__main__":
    unittest.main()