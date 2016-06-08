from Effect import *
from card import *
from random import *
from pygame import *
from Buffs import *
from Buff import *
from DrawBoard import *
from Damage import *

class GRM_EFF(Effect):
    
    def __init__ (self, board, card):
        self.played = True
        self.endTurn = False
        self.beginTurn = False
        self.board = board
        self.host = card
        
    def onPlay(self):
        spots = self.board.getSpots()
        for i in range (2):
            for j in range (7):
                if spots[i][j].getOccupied():
                    card = spots[i][j].getCard()
                    if card.getCreatureType() == "Murloc" and card != self.host:
                        curBuff = GRM_BUFF(card, self.board)
                        card.addBuff(curBuff)
                        curBuff.applyBuff()
                        
                        
    def playCreature(self, card):
        if card.getCreatureType() == "Murloc" and card != self.host:
                        curBuff = GRM_BUFF(card, self.board)
                        card.addBuff(curBuff)
                        curBuff.applyBuff()
                        
    def killCreature(self, card):
        if card == self.host:
            spots = self.board.getSpots()
            for i in range (2):
                for j in range (7):
                    if spots[i][j].getOccupied():
                        onlyOne = True
                        card = spots[i][j].getCard()
                        for buff in card.getBuffs():
                            if type(buff) == type(GRM_BUFF(None,None)) and onlyOne:
                                onlyOne = False
                                buff.removeBuff()
            self.board.effects.remove(self)
        
    
    