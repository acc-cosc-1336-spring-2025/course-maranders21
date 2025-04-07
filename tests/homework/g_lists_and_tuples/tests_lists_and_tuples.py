#
import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value
from src.homework.g_lists_and_tuples.lists import get_highest_list_value

class Test_Config(unittest.TestCase):
    def test_get_lowest_list_value_1(self):
        #test that the function get_lowest_list_value returns 1
        self.assertEqual(1, get_lowest_list_value([8,10,1,50,20]))
    
    def test_get_highest_list_value_1(self):
        #test that the function get_highest_list_value returns 50
        self.assertEqual(50, get_highest_list_value([8,10,1,50,20]))