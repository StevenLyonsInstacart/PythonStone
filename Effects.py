from pygame import *
from random import *

from Buff import *
from Buffs import *
from Damage import *
from DrawBoard import *
from Effect import *
from card import *
from Constants import *

# Grimscale oracle effect
# While Grimscale Oracle is in play, all other murlocs gain +1 attack

class GRM_EFF(Effect):
    
    def __init__ (self, board, card):
        self.played = True
        self.endTurn = False
        self.beginTurn = False
        self.board = getBoard()
        self.host = card
        
    #On play give each other Murloc +1 attack
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
                        
    #On another creature being played, check if its a murloc and give buff if needed                    
    def playCreature(self, card):
        if card.getCreatureType() == "Murloc" and card.getID() != self.host.getID():
                        curBuff = GRM_BUFF(card, self.board)
                        card.addBuff(curBuff)
                        curBuff.applyBuff()
     
    #When the Grimscale oracle dies, remove the buff from all other murlocs                    
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
            
class SPELL_DAMAGE(Effect):
    
    def __init__ (self, board, card, spellDamage):
        self.played = True
        self.endTurn = False
        self.beginTurn = False
        self.board = getBoard()
        self.host = card
        self.damage = spellDamage
            
        #On play give each other Murloc +1 attack
    def onPlay(self):
        self.host.getPlayer().addSpellDamage(self.damage)
        
    def playCreature(self, card):
        pass
     
    #When the Grimscale oracle dies, remove the buff from all other murlocs                    
    def killCreature(self, card):
        if card == self.host:
            self.host.getPlayer().addSpellDamage(-self.damage)
            self.board.effects.remove(self)
    
    