import unittest
import sys, os

sys.path.append(os.getcwd())
from builder import *

class TestCost(unittest.TestCase):

    def test_cost(self):
        self.assertEqual(check_cost("Huawei 50 Lite"), 25000)

if __name__ == "__main__":
    unittest.main()
