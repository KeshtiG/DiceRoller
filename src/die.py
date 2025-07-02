#!/usr/bin/env python3
"""
Contains the Die class.
"""

import random

class Die():
    """
    Creates a die with a value between 1 and 6.
    """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6

    def __init__(self, value = None):
        if value is None:
            self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)

        elif value > self.MAX_ROLL_VALUE:
            self._value = self.MAX_ROLL_VALUE

        elif value < self.MIN_ROLL_VALUE:
            self._value = self.MIN_ROLL_VALUE

        else:
            self._value = value

    def get_value(self):
        """ Returns the value. """
        return self._value

    def get_name(self):
        """ Returns the number name as a string. """
        name_list = ["one", "two", "three", "four", "five", "six"]
        name_dict = dict(enumerate(name_list, 1))
        name = name_dict[self.get_value()]

        return name

    def roll(self):
        """ Generates a new random value. """
        self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)

    def __str__(self):
        value = self.get_value()
        return str(value)
