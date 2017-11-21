# -*- coding: utf-8 -*-
"""
@author: Andrew McClement
"""
import uuid


class Role:
    def __init__(self, char_name, power, personal_goal):
        self.name = char_name
        self.power = power
        self.goal = personal_goal
        self.Id = uuid.uuid4()

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

    def __init__(self, power):
        self.power = power
        self.players = {}

    def add_player(self, player):
        self.players[player.name] = player


class PowerRestriction:
    def __init__(self, game):
        self.game = game


class Player:
    _all_players_by_name = {}

    def __init__(self, name, game):
        self.name = name
        self.game = game
        # Names must be unique.
        assert(name not in self._all_players_by_name)
        self._all_players_by_name[name] = self

    def define_role(self, role):
        self.role = role


class RtwGame:
    def __init__(self):
        self._players = {}
        self._roles = {}

    def add_player(self):
        print("Set up a new player")
        name = input("Name: ")
        self._add_player(name)

    def _add_player(self, name):
        player = Player(name, self)
        self._players[name] = player

    def create_role(self):
        name = input("Please enter the character name: ")
        power = self.create_power()
        personal_goal = input("Please type the personal goal: ")
        role = Role(name, power, personal_goal)
        self._roles[role.Id] = role

    def create_power(self):
        pass


if __name__ == "__main__":
    pass
