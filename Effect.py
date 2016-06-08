from card import *
from random import *
from pygame import *
from Buffs import *
from Buff import *
from DrawBoard import *
from Damage import *

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
        
    