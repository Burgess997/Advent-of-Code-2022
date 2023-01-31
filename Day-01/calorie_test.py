import unittest
from calorie import FindMostCalories

class TestFindMostCalories(unittest.TestCase):
    def test_example(self):
        self.assertEqual(FindMostCalories([1000,2000,3000,"",4000,"",5000,6000,"",7000,8000,9000,"",10000]), 24000)