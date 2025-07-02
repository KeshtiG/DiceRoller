#!/usr/bin/env python3
"""
Contains the Hand class.
"""
from src.die import Die

class Hand():
    """ Creates and handles a set of 5 dices. """
    def __init__(self, dice_values=None):
        # Create empty lists
        self.dice = []

        # If no values are sent, create new dice objects
        if dice_values is None:
            for _ in range(5):
                self.dice.append(Die())
        # If values are sent, create dice objects with the values
        else:
            for value in dice_values:
                self.dice.append(Die(value))

    def roll(self, indexes=None):
        """ Generates new values for selected indexes. """
        # If no indexes are sent, roll all dice
        if indexes is None:
            for die in self.dice:
                die.roll()

        # If indexes are sent, roll the dice at the indexes
        else:
            for index in indexes:
                self.dice[index].roll()

    def __str__(self):
        str_list = []
        # Loop through the dice and add them to the list
        for dice in self.dice:
            str_list.append(str(dice))

        # Join the list to a string
        dice_str = ", ".join(str_list)

        return dice_str
