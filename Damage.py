from pygame import *
from card import *
from Grid import *
from cards import *
from random import *
from Turn import *
from DrawBoard import *
from Spot import *

def dealDamage(target, total, board):
    target.getCard().takeDamage(total)
    if target.getCard().getToughness() <= 0:
	board.cardDeath(target.getCard())
        target.setCard(NULL_CR())
	target.getCard().clearBuffs()
	target.setOccupied(False)
	
        
class NULL_CR(Creature):
    def __init__(self):
        self.name = "Null"
        self.power = 0
        self.toughness = 0
        self.cost = 0
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
	self.buffs = []