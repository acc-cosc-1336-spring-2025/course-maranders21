#
import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value
from src.homework.g_lists_and_tuples.lists import get_highest_list_value
from src.homework.g_lists_and_tuples.tuples import get_p_distance
from src.homework.g_lists_and_tuples.tuples import get_p_distance_matrix

class Test_Config(unittest.TestCase):
    def test_get_lowest_list_value_1(self):
        #test that the function get_lowest_list_value returns 1
        self.assertEqual(1, get_lowest_list_value([8,10,1,50,20]))
    
    def test_get_highest_list_value_1(self):
        #test that the function get_highest_list_value returns 50
        self.assertEqual(50, get_highest_list_value([8,10,1,50,20]))

    def test_get_p_distance_1(self):
        #test that the function get_p_distance returns value 0.4
        self.assertEqual(0.4, get_p_distance(['T','T','T','C','C','A','T','T','T','A'], ['G','A','T','T','C','A','T','T','T','C']))

    def test_get_p_distance_matrix_1(self):
        #test that the function get_p_distance_matrix returns value:
        """[
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]"""
        self.assertEqual([[0.0, 0.4, 0.1, 0.1], 
                          [0.4, 0.0, 0.4, 0.3], 
                          [0.1, 0.4, 0.0, 0.2], 
                          [0.1, 0.3, 0.2, 0.0]],
                          get_p_distance_matrix([['T','T','T','C','C','A','T','T','T','A'], 
                           ['G','A','T','T','C','A','T','T','T','C'], 
                           ['T','T','T','C','C','A','T','T','T','T'], 
                           ['G','T','T','C','C','A','T','T','T','A']]))