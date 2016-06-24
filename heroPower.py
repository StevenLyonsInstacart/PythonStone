from pygame import *
from random import *

from Buff import *
from Buffs import *
from Damage import *
from DrawBoard import *
from Effect import *
from Effects import *
from Health import *
from Weapon import *
from card import *
from cards import *
from spawn import *

#Hero power class
class heroPower():
    
    # Name: The Name of the ability
    # className: The string representation of the class associated with the power
    # player: the player who has the hero power
    def __init__(self, name, className, player):
        self.name = name
        self.className = className
        # cost is by default set to 2
        self.cost = 2
        # tired is set by default to false, as hero powers dont have summoning sickness
        self.tired = False
        self.player = player
        
    def doPower(self):
        pass
    
    ########################
    #    Get Statements    #
    ########################
    
    def getName(self):
        return self.name
    def getClassName(self):
        return self.ClassName
    def getCost(self):
        return self.cost
    def getTired(self):
        return self.tired
    def getplayer(self):
        return player
    
    ########################
    #    Set Statements    #
    ########################
    def setName(self, name):
        self.name = name
    def setClassName(self, className):
        self.ClassName = name
    def setCost(self, cost):
        self.cost = cost
    def setTired(self, tired):
        self.tired = tired
        
# Deal two damage to the Enemy hero        
class HunterPower(heroPower):
    
    def __init__(self, player):
        heroPower.__init__(self, "Steady Shot", "Hunter", player)
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
            self.player.getEnemy().incLife(-2)

#Draw a card and lose two life            
class WarlockPower(heroPower):
    
    def __init__(self, player):
        heroPower.__init__(self, "Life Tap", "Warlock", player)
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
            self.player.incLife(-2)
            self.player.draw()

#Gain 1 armor and 1 attack	    
class DruidPower(heroPower):
    
    def __init__(self, player):
        heroPower.__init__(self, "Druidia", "Druid", player)
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
	    self.player.changeCurMana(-self.cost)
            self.player.changeArmor(1)
            self.player.setPower(self.player.getPower() + 1)
            
# Gain two armor	    
class WarriorPower(heroPower):
    
    def __init__(self, player):
        heroPower.__init__(self, "Armor Up", "Warrior", player)
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
	    self.player.changeCurMana(-self.cost)
            self.player.changeArmor(2)
            
#Deal 1 damage to a minion or player            
class MagePower(heroPower):
    
    def __init__(self, player, screen, board):
        heroPower.__init__(self, "Fireball", "Mage", player)
        self.screen = screen
	self.board = board
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
	    target, typ = SelectTarget(self.board, self.screen, "abusive_sergeant.png", self.player, self.player.getEnemy() )
	    if typ == "Creature":
		dealDamage(target, 1, self.board)
	    else:
		if target == self.player.getOrder():
		    burstFace(self.player, 1)
		else:
		    burstFace(self.player.getEnemy(), 1)
            
# Summon a silver hand recruit	    
class PaladinPower(heroPower):
    def __init__(self, player, board):
        heroPower.__init__(self, "Call to Arms", "Paladin", player)
	self.board = board
	
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
	    spawnCreature(DUDE(), self.player.getEnemy().getSpots(), self.board)
        
# Equip a Dagger	    
class RoguePower(heroPower):
    def __init__(self, player):
        heroPower.__init__(self, "Daggers Yo", "Rogue", player)
	
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
	    self.player.armed()
	    self.player.setWeapon(Dagger())
        
# Heal yourself for two life	    
class PriestPower(heroPower):
    def __init__(self, player, screen, board):
        heroPower.__init__(self, "The Light Shall Burn You", "Priest", player)
	self.board = board
	self.screen = screen
	
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
	    target, typ = SelectTarget(self.board, self.screen, "abusive_sergeant.png", self.player, self.player.getEnemy() )
	    if typ == "Creature":
		healCreature(target.getCard(), 2)
	    else:
		if target == self.player.getOrder():
		    self.player.heal(2)
		else:
		    self.player.getEnemy().heal(2)
    
# Select either a minion or a hero
# Returns a target and a classifier

def SelectTarget(board, screen, filename, player, enemy):	
    waiting = True
    spots = board.getSpots()
    while waiting:
	
	for evnt in event.get():
	    
	    if evnt.type == MOUSEBUTTONDOWN:
		mx, my = evnt.pos
		for i in range (2):
		    for j in range(0,7):
			if 200*j < mx < 200*(j+1) and 150 + 250*(i) < my < 150 + 250*(i+1):
			    square = [i,j]
			    reversei = abs(1-i)
			    if spots[reversei][j].getOccupied():
				return spots[reversei][j], "Creature"
		for i in range (2):
		    if 550 < mx < 850 and 100 + 500*i < my < 200 + i*500:
			return i, "Player"
			
	    elif evnt.type == MOUSEMOTION:
		drawGrid(screen, board, filename)
		showBoard(board.getSpots(), screen)
		showHand(board.getHands(), screen, 0)
		highlight((255, 255, 0), evnt.pos, screen)
	    display.flip()
	    

#A highlight function which only works on minions on the board or heroes
def highlight(colour, pos, screen):
    for i in range (0,7):
	if pos[1] > 200 and pos[1] < 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
	    draw.rect(screen, colour, (200*i,200, 200, 200), 10)
	if pos[1] < 600 and pos[1] > 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
	    draw.rect(screen, colour, (200*i,400, 200, 200), 10)    
    for i in range (2):
	if 550 < pos[0] < 850 and 100 + 500*i < pos[1] < 200 + i*500:
	    draw.rect(screen, colour, (550,100 + 500*i, 300, 100), 10)
            
        