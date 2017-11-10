# -*- coding: utf-8 -*-
"""
@author: Andrew McClement
"""


class Role:
    def __init__(self, char_name, power, personal_goal):
        self.name = char_name
        self.power = power
        self.goal = personal_goal

    def use_power(self, targets=[]):
        self.power(*targets)


class Power:
    def __init__(self, restrictions, effect):
        pass


# Not used at present.
class Team:
    """
    A class for allowing team actions to be made.
    """

    def __init__(self, players, power):
        self.players = players
        self.power = power


class PowerRestriction:
    def __init__(self, game):
        self.game = game


class Player:
    def __init__(self, name, game, role):
        self.name = name
        self.game = game
        self.role = role


class RtwGame:
    pass



if __name__ == "__main__":
    pass
