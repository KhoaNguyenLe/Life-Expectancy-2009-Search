import pymongo
import unittest
from find import *

state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]


class TestFind(unittest.TestCase):

    def test_find_state_overall(self):
        f = Find()
        
        self.assertEqual(76.5, f.find_state_overall("Texas"))
        self.assertEqual(78.6, f.find_state_overall("Utah"))
        self.assertEqual(71.9, f.find_state_overall("Mississippi"))
        self.assertEqual(77.5, f.find_state_overall("Florida"))
        self.assertEqual(74.1, f.find_state_overall("Oklahoma"))
        self.assertEqual(76.4, f.find_state_overall("Kansas"))
        self.assertEqual(76.8, f.find_state_overall("Maryland"))
        self.assertEqual(76.8, f.find_state_overall("Montana"))
        self.assertEqual(78.4, f.find_state_overall("Idaho"))
        self.assertEqual(80.7, f.find_state_overall("Hawaii"))
        self.assertEqual(78.3, f.find_state_overall("Colorado"))

    def test_find_state_male(self):
        f = Find()
        self.assertEqual(73.7, f.find_state_male("Texas"))
        self.assertEqual(76.7, f.find_state_male("Utah"))
        self.assertEqual(68.6, f.find_state_male("Mississippi"))
        self.assertEqual(74.6, f.find_state_male("Florida"))
        self.assertEqual(71.5, f.find_state_male("Oklahoma"))
        self.assertEqual(73.8, f.find_state_male("Kansas"))
        self.assertEqual(73.8, f.find_state_male("Maryland"))
        self.assertEqual(74.2, f.find_state_male("Montana"))
        self.assertEqual(76.1, f.find_state_male("Idaho"))
        self.assertEqual(77.6, f.find_state_male("Hawaii"))
        self.assertEqual(75.8, f.find_state_male("Colorado"))

    def test_find_state_female(self):
        f = Find()
        self.assertEqual(79.3, f.find_state_female("Texas"))
        self.assertEqual(80.6, f.find_state_female("Utah"))
        self.assertEqual(75.2, f.find_state_female("Mississippi"))
        self.assertEqual(80.5, f.find_state_female("Florida"))
        self.assertEqual(76.9, f.find_state_female("Oklahoma"))
        self.assertEqual(79.2, f.find_state_female("Kansas"))
        self.assertEqual(79.7, f.find_state_female("Maryland"))
        self.assertEqual(79.6, f.find_state_female("Montana"))
        self.assertEqual(80.8, f.find_state_female("Idaho"))
        self.assertEqual(83.8, f.find_state_female("Hawaii"))
        self.assertEqual(80.9, f.find_state_female("Colorado"))

    def test_find_average(self):
        f = Find()

        self.assertAlmostEqual(73.85, f.find_average("Male"), 2)
        self.assertAlmostEqual(79.44, f.find_average("Female"), 2)
        self.assertAlmostEqual(76.60, f.find_average("Total"), 2)

    def test_find_highest(self):
        f = Find()

        self.assertEqual(('Hawaii', 77.6), f.find_highest("Male"))
        self.assertEqual(('Hawaii', 83.8), f.find_highest("Female"))
        self.assertEqual(('Hawaii', 80.7), f.find_highest("Total"))

    def test_find_lowest(self):
        f = Find()
        self.assertEqual(('Mississippi', 68.6), f.find_lowest("Male"))
        self.assertEqual(('Mississippi', 75.2), f.find_lowest("Female"))
        self.assertEqual(('Mississippi', 71.9), f.find_lowest("Total"))