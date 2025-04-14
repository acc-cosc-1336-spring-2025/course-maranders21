#
import unittest
#src/homework/i_dictionaries_sets/dictionary.py
from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget
inventory_dictionary = {}


class Test_Config(unittest.TestCase):
    def test_add_inventory_1(self):
        #test that the function returns 10 under key Widget1
        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertEqual(10, inventory_dictionary["Widget1"])

    def test_add_inventory_2(self):
        #test that the function returns 35 under key Widget1
        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(35, inventory_dictionary["Widget1"])

    def test_add_inventory_3(self):
        #test that the function returns 35 under key Widget1
        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(25, inventory_dictionary["Widget1"])

    def test_remove_inventory_widget_1(self):
        #test that the function returns a dictionary length of 1
        #test that the function returns True - if widget2 exists
        test_dictionary = {}
        add_inventory(test_dictionary, "widget1", 1)
        add_inventory(test_dictionary, "widget2", 2)
        self.assertEqual("Record deleted", remove_inventory_widget(test_dictionary, "widget1"))
        self.assertEqual(1, len(test_dictionary))
        self.assertEqual(True, "widget2" in test_dictionary)