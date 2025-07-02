#!/usr/bin/env python3
"""
Module for testing the class Die.
"""

import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """
    Test class for the Die class.
    """
    def test_create_die_without_arguments(self):
        """ Test that a die object can be created without arguments. """
        random.seed(69)
        die = Die()
        self.assertEqual(die.get_value(), 6, "Should be 6.")

    def test_create_die_with_value(self):
        """ Test that a die object can be created with a value. """
        die = Die(3)
        self.assertEqual(die.get_value(), 3)

    def test_create_die_high_value(self):
        """ Test that a die object created with a value higher than 6 is set to max 6. """
        die = Die(999)
        self.assertEqual(die.get_value(), 6)

    def test_create_die_low_value(self):
        """ Test that a die object created with a value lower than 1 is set to min 1. """
        die = Die(-50)
        self.assertEqual(die.get_value(), 1)

    def test_roll_changes_value(self):
        """ Test that rolling the die changes its value. """
        random.seed(69)

        die = Die(2)
        org_value = die.get_value()

        die.roll()
        new_value = die.get_value()

        self.assertNotEqual(org_value, new_value, "The method should create a new value.")

    def test_get_name(self):
        """Test that get_name() returns the correct name."""
        die_names = ["one", "two", "three", "four", "five", "six"]

        for number in range(1, 7):
            die = Die(number)
            self.assertEqual(die.get_name(), die_names[number - 1])

    def test_string_die(self):
        """
        Test that the die value is printed as a string.
        """
        die = Die(6)
        self.assertEqual(str(die), "6")
