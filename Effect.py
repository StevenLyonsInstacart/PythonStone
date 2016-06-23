from pygame import *
from random import *

from Buff import *
from Buffs import *
from Damage import *
from DrawBoard import *
from card import *


class Effect:
    
    def __init__(self, board):
        self.played = False
        self.endTurn = False
        self.beginTurn = False
        self.board = board
        
    def OnPlay(self):
        pass
    
    def End(self):
        pass
    
    def endTurn(self):
        pass
    
    def beginTurn(self):
        pass
    
    def playCreature(self):
        pass
    
    def killCreature(self):
        pass
        
    