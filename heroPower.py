from pygame import *
import random

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
from Constants import *

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
            
# Deal two damage to the Enemy hero        
class ShamanPower(heroPower):
    
    def __init__(self, player):
        heroPower.__init__(self, "Totemic Call", "Shaman", player)
        self.board = getBoard()
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            totems = [STN_TOT(), SEA_TOT(), AIR_TOT()]
            ind = int(random()*3)
            totems[ind].setPlayer(self.player)
            spawnCreature(totems[ind], self.player.getEnemy().getSpots(), self.board, 6)
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
    
    def __init__(self, player):
        heroPower.__init__(self, "Fireball", "Mage", player)
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
            target, typ = SelectTarget("abusive_sergeant.png", self.player, self.player.getEnemy() )
            if typ == "Creature":
                dealDamage(target, 1, getBoard())
            else:
                if target == self.player.getOrder():
                    burstFace(self.player, 1)
                else:
                    burstFace(self.player.getEnemy(), 1)
            
# Summon a silver hand recruit	    
class PaladinPower(heroPower):
    def __init__(self, player):
        heroPower.__init__(self, "Call to Arms", "Paladin", player)
        self.board = getBoard()
	
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
            spawnCreature(DUDE(), self.player.getEnemy().getSpots(), self.board, 6)
        
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
    def __init__(self, player):
        heroPower.__init__(self, "The Light Shall Burn You", "Priest", player)

	
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
            target, typ = SelectTarget("abusive_sergeant.png", self.player, self.player.getEnemy() )
            if typ == "Creature":
                healCreature(target.getCard(), 2)
            else:
                if target == self.player.getOrder():
                    self.player.heal(2)
                else:
                    self.player.getEnemy().heal(2)
    
# Select either a minion or a hero
# Returns a target and a classifier

def SelectTarget(filename, player, enemy):
    board = getBoard()
    screen = getScreen()	
    waiting = True
    spots = board.getSpots()
    
    convx = screen.get_width() / 1600.0
    convy = screen.get_height() / 800.0
    
    while waiting:
	
        for evnt in event.get():
	    
            if evnt.type == MOUSEBUTTONDOWN:    
                mx, my = evnt.pos
                for i in range (2):
                    for j in range(0,7):
                        if convx*200*j < mx < convx*200*(j+1) and convy*(150 + 250*(i)) < my < convy*(150 + 250*(i+1)):
                            square = [i,j]
                            reversei = abs(1-i)
                            if spots[reversei][j].getOccupied():
                                return spots[reversei][j], "Creature"
                for i in range (2):
                    if convx*550 < mx < convx*850 and convy*(100 + 500*i) < my < convy*(200 + i*500):
                        return i, "Player"
			
            elif evnt.type == MOUSEMOTION:
                drawGrid(filename)
                showBoard(board.getSpots())
                showHand(board.getHands(), getTurn())
                highlight((255, 255, 0), evnt.pos)
	    display.flip()
	    

#A highlight function which only works on minions on the board or heroes
def highlight(colour, pos):
    screen = getScreen()
    convx = screen.get_width() / 1600.0
    convy = screen.get_height() / 800.0
    
    for i in range (0,7):
        if pos[1] > 200*convy and pos[1] < 400*convy and pos[0]> i*200*convx and pos[0] < (i+1)*200*convx:
            draw.rect(screen, colour, (200*i*convx,200*convy, 200*convx, 200*convy), 10)
        if pos[1] < 600*convy and pos[1] > 400*convy and pos[0]> i*200*convx and pos[0] < (i+1)*200*convx:
            draw.rect(screen, colour, (200*i*convx,400*convy, 200*convx, 200*convy), 10)  
    for i in range (2):
        if convx*550 < pos[0] < convx*850 and convy*(100 + 500*i) < pos[1] < convy*(200 + i*500):
            draw.rect(screen, colour, (convx*550,convy*(100 + 500*i), convx*300, convy*100), 10)
            
        