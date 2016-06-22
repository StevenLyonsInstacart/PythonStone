from card import *
from random import *
from pygame import *
from Buffs import *
from Buff import *
from DrawBoard import *
from Damage import *
from Effect import *
from Effects import *
from heroPower import *

class Player:
    
    def __init__(self, hand, deck, spots, mana, order, role="None"):
        self.hand = hand
        self.deck = deck
        self.spots = spots
        self.role = role
        self.portrait = "guldan_portrait.jpg"
        self.life = 30
        self.enemy = None
        self.hp = None
        self.order = order
        self.curMana = mana
        self.totMana = mana
        self.power = 0
        self.ready = True
        self.armor = 0
        self.weapon = None
        self.hasWeapon = False
        
    def isReady(self):
        return self.ready
    def getPower(self):
        return self.power
    def getHand(self):
        return self.hand
    def getDeck(self):
        return self.deck
    def getSpots(self):
        return self.spots
    def getRole(self):
        return self.role
    def getPortrait(self):
        return self.portrait
    def getLife(self):
        return self.life
    def getEnemy(self):
        return self.enemy
    def getHP(self):
        return self.hp
    def getOrder(self):
        return self.order
    def getArmor(self):
        return self.armor
    def getWeapon(self):
        return self.weapon
    
    def armed(self):
        self.hasWeapon = True
    def isArmed(self):
        return self.hasWeapon
    def unarmed(self):
        self.hasWeapon = False
    
    
    def setHand(self, hand):
        self.hand = hand
    def setDeck(self, deck):
        self.deck = deck
    def setSpots(self, spots):
        self.spots = spots
    def setRole(self, role):
        self.role = role
    def setPortrait(self, port):
        self.portrait = port
    def setLife(self, life):
        self.life = life
    def setEnemy(self, player):
        self.enemy = player
    def setHP(self, power):
        self.hp = power
    def setPower(self, power):
        self.power = power
    def setReady(self, ready):
        self.ready = ready
    def setWeapon(self, weapon):
        self.weapon = weapon
        if weapon:
            self.power += weapon.getPower()
        else:
            self.power = 0
        
    def getTotalMana(self):
        return self.totMana
    def getCurMana(self):
        return self.curMana
        
    def changeCurMana(self, change):
        self.curMana = self.curMana + change
    def changeTotMana(self, change):
        self.totMana = self.totMana + change
        if self.totMana > 10:
            self.totMana = 10
            
    def changeArmor(self, inc):
        output = min(0, self.armor +inc)
        self.armor = max(0, self.armor +inc)
        return output
    
    def startTurn (self):
        self.curMana = self.totMana
    
    def doHeroPower(self):
        if not (self.hp.getTired()):
            self.hp.doPower()
            self.hp.setTired(True)
        
    def incLife(self, inc):
        if self.armor > 0:
            lifeDeduct = self.changeArmor(inc)
            self.life = self.life + lifeDeduct
        else:
            self.life += inc
        
    def setEnemies(self, player):
        self.enemy = player
        player.setEnemy(self) 
        
    def draw(self):
        self.hand.draw(self.deck)
    
    