import unittest
from unitesting_file import eat,check_num


class Testactivity(unittest.TestCase):
    
    def test_eats(self):
        """this is veg"""
        self.assertEqual(
            eat("veg",ishealthy=True),
            "veg food is healthy"
        )
    
    def test_eat(self):
        """this is non veg"""
        self.assertEqual(
            eat("non-veg",ishealthy=False),
            "lol"
        )
      
        
    def test_check_num(self):
        """this is 3"""
        self.assertEqual(
        check_num(3),
        "this is 3"
        )
        
    def test_num(self):
        """this is 1"""
        self.assertEqual(
           check_num(1),
            "this is 1"
        )
       
if __name__=="__main__":
    unittest.main()