#!/usr/bin/python3
"""Darrin Bliler
   Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model
   Cheat_Mulligan(Player) - Subclass model"""

from random import randint
from cheatdice import Player

class Cheat_Mulligan(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if sum(self.dice) < 9:
                self.dice[i] = (randint(1,6))
            i += 1