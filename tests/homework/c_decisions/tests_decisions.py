#
import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio_1(self):
        #test that the function get_options_ratio returns 0.25
        self.assertEqual(0.25, get_options_ratio(5,20))
    
    def test_get_options_ratio_2(self):
        #test that the function get_options_ratio returns 0.5
        self.assertEqual(0.5, get_options_ratio(10,20))

    def test_get_faculty_rating_1(self):
        #test that the function get_faculty_rating returns "Excellent"
        self.assertEqual("Excellent", get_faculty_rating(0.91))

    def test_get_faculty_rating_2(self):
        #test that the function get_faculty_rating returns "Very Good"
        self.assertEqual("Very Good", get_faculty_rating(0.85))

    def test_get_faculty_rating_3(self):
        #test that the function get_faculty_rating returns "Good"
        self.assertEqual("Good", get_faculty_rating(0.71))

    def test_get_faculty_rating_4(self):
        #test that the function get_faculty_rating returns "Needs Improvement"
        self.assertEqual("Needs Improvement", get_faculty_rating(0.66))

    def test_get_faculty_rating_5(self):
        #test that the function get_faculty_rating returns "Unacceptable"
        self.assertEqual("Unacceptable", get_faculty_rating(0.45))