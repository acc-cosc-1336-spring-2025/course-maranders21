#
import unittest
from src.homework.j_classes import class_a

class Test_Config(unittest.TestCase):
    def test_Die_1(self):
        test_1 = class_a.Die()
        test_1.roll()
        test_result_1 = False
        if test_1.get_rolled_value() >= 1 and test_1.get_rolled_value() <= 6:
            test_result_1=True
        self.assertEqual(True, test_result_1)
        
    def test_Die_2(self):
        test_2 = class_a.Die()
        test_2.roll()
        test_result_2 = False
        if test_2.get_rolled_value() >= 1 and test_2.get_rolled_value() <= 6:
            test_result_2=True
        self.assertEqual(True, test_result_2)
    
    def test_Die_3(self):
        test_3 = class_a.Die()
        test_3.roll()
        test_result_3 = False
        if test_3.get_rolled_value() >= 1 and test_3.get_rolled_value() <= 6:
            test_result_3=True
        self.assertEqual(True, test_result_3)
        