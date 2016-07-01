from pygame import *
from random import *

from DrawBoard import *
from Spot import *
from Turn import *
from card import *
from cards import *

#All damage done in the game should come from a method in this File,
#Because if it doesn't it might miss a trigger

# Deal damage deals total damage to the card in spot Target, and triggers any
# abilities related to this
# target: a spot holding the card recieving damage
# total: int amount of damage dealt
# board: a reference to the board

def dealDamage(target, total, board):
    target.getCard().takeDamage(total)
    if target.getCard().getToughness() <= 0:
        if target.getCard().hasDeathRattle():
            target.getCard().deathRattle()
        if target.getCard().hasTaunt():
            if target.getCard() in board.getCurrentPlayer().getTaunts():
                board.getCurrentPlayer().removeTaunt(target.getCard())
            if target.getCard() in board.getEnemyPlayer().getTaunts():
                board.getEnemyPlayer().removeTaunt(target.getCard())
        board.cardDeath(target.getCard())
        target.setCard(NULL_CR())
        target.getCard().clearBuffs()
        target.setOccupied(False)
	
#Fight allows two minions two deal damage to each other
def fight(spot1, spot2, board):
    attacker = spot1.getCard()
    defender = spot2.getCard()
    defender.setTired(True)
    attackPower = attacker.getPower()
    dealDamage(spot1, defender.getPower(), board)
    dealDamage(spot2, attacker.getPower(), board)
    
#For damage from a creature to a player    
def goFace(creature, player):
    player.incLife(-creature.getPower())
    creature.setTired(True)
    if player.getLife() < 1:
        quit()
        
#For damage from a non-minion source to a player	
def burstFace(player, inc):
    player.incLife(-inc)
    if player.getLife() < 1:
        quit()

#For damage from a face to a minion	
def faceGo(player, spot, board):
    burstFace(player, spot.getCard().getPower())
    dealDamage(spot, player.getPower(), board)

#Player to Player damage    
def faceToFace(player1, player2):
    burstFace(player1, player2.getPower())
    player2.setReady(False)
    
    
        
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