import unittest

'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.b_in_proc_out.output import get_number
from src.homework.b_in_proc_out.output import multiply_numbers

class Test_Config(unittest.TestCase):

    def test_get_number_1(self):
        #test that the function get_number returns 1
        self.assertEqual(1, get_number(1))
    
    def test_get_number_2(self):
        #test that the function get_number returns 2
        self.assertEqual(2, get_number(2))

    def test_multiply_numbers_1 (self) :
        self.assertEqual(25,multiply_numbers(5,5))
        
    def test_multiply_numbers_2 (self) :
        self.assertEqual(100,multiply_numbers(10,10))

