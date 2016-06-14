from card import *
from random import *
from pygame import *
from Buffs import *
from Buff import *
from DrawBoard import *
from Damage import *
from Effect import *
from Effects import *


class heroPower():
    
    def __init__(self, name, className, player):
        self.name = name
        self.className = className
        self.cost = 2
        self.tired = False
        self.player = player
        
    def doPower(self):
        pass
    
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
    
    def setName(self, name):
        self.name = name
    def setClassName(self, className):
        self.ClassName = name
    def setCost(self, cost):
        self.cost = cost
    def setTired(self, tired):
        self.tired = tired
        
class HunterPower(heroPower):
    
    def __init__(self, player):
        heroPower.__init__(self, "Steady Shot", "Hunter", player)
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
            self.player.getEnemy().incLife(-2)
            
class WarlockPower(heroPower):
    
    def __init__(self, player):
        heroPower.__init__(self, "Life Tap", "Warlock", player)
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
            self.player.incLife(-2)
            self.player.draw()
            
class MagePower(heroPower):
    
    def __init__(self, player, screen):
        heroPower.__init__(self, "Fireball", "Mage", player)
        self.screen = screen
        
        
    def doPower(self):
        if self.player.getCurMana() >= self.cost:
            self.player.changeCurMana(-self.cost)
            while True:
                highlight((255, 255, 0), evnt.pos, screen)
            
        