from pygame import *
from card import *
from cards import *
from random import *
from Turn import *
from DrawBoard import *
from Spot import *

def dealDamage(target, total, board):
    target.getCard().takeDamage(total)
    if target.getCard().getToughness() <= 0:
	if target.getCard().hasDeathRattle():
	    target.getCard().deathRattle()
	board.cardDeath(target.getCard())
        target.setCard(NULL_CR())
	target.getCard().clearBuffs()
	target.setOccupied(False)
	
def fight(spot1, spot2, board):
    attacker = spot1.getCard()
    defender = spot2.getCard()
    defender.setTired(True)
    attackPower = attacker.getPower()
    dealDamage(spot1, defender.getPower(), board)
    dealDamage(spot2, attacker.getPower(), board)
    
def goFace(creature, player):
    player.incLife(-creature.getPower())
    creature.setTired(True)
    if player.getLife() < 1:
	quit()
	
def burstFace(player, inc):
    player.incLife(-inc)
    if player.getLife() < 1:
	quit()
    
    
        
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