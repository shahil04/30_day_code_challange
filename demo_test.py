import unittest
from demo import eat,num

class DemoTest(unittest.TestCase):
    
    def test_eat(self):
        self.assertEqual(
                eat("challi",ishealthy=True),
                "challi"
            )
    def test_uneat(self):    
        self.assertEqual(
                eat("tea",ishealthy=False),
                "tea"
            )
        
        
if __name__=="__main__":
    unittest.main()