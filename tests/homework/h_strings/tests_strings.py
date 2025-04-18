#
import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):
    def test_get_hamming_distance_1(self):
        #test that the function get_hamming_distance returns 7
        self.assertEqual(7, get_hamming_distance("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))
    
    def test_get_dna_complement_1(self):
        #test that the function get_dna_complement returns ACCGGGTTTT
        self.assertEqual("ACCGGGTTTT", get_dna_complement("AAAACCCGGT"))