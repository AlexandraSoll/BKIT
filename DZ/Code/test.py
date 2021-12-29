import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class Test_bikvadrat(unittest.TestCase):
    def test_a_equal_zero(self):
        self.assertEqual(a_equal_zero("0"), 1)
        self.assertEqual(a_equal_zero("3242432"), 0)

    def test_result_bikvadrat(self):
        self.assertEqual(bikvadrat(1, -2, 1), [1, -1])
        self.assertEqual(bikvadrat(1, 0, -4), [1.4142135623730951, -1.4142135623730951])
