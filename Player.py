from pygame import *
from random import *

from Buff import *
from Buffs import *
from Damage import *
from DrawBoard import *
from Effect import *
from Effects import *
from card import *
from heroPower import *

# A representation of a player
class Player:
    
    # hand: the player's hand (hand)
    # deck: the plaeyr's deck (deck)
    # spots: spots on the player's portion of the board ([Spot])
    # mana: the initial mana the player has (int)
    # order: whether they start or go second (int)
    # portrait: The filename of the champion portrait (String)
    # life: current life (int)
    # enemy: the enemy player (Player)
    # hp: The Player's heropower (HeroPower)
    # curMana: The Player's current useable Mana
    # totMana: The number of mana crystals the player has
    # power: The Player's power (int)
    # ready: Bbool if the player can attck
    # armor: the player's armor (int)
    # weapon: The player's weapon (Weapon)
    # hasWeapon: if the player has a weapon (Bool)
    
    def __init__(self, hand, deck, spots, mana, order, role="None"):
        self.hand = hand
        self.deck = deck
        self.spots = spots
        self.role = role
        self.portrait = "blanks/guldan_portrait.jpg"
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
    
    #####################
    #    Get Methods    #
    #####################
    
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
    def getTotalMana(self):
        return self.totMana
    def getCurMana(self):
        return self.curMana
    
    #####################
    #    Set Methods    #
    #####################
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
        if self.weapon:
            self.power -= self.weapon.getPower()
        self.weapon = weapon
        if weapon:
            self.power += weapon.getPower()
        else:
            self.power = 0
    def setEnemies(self, player):
        self.enemy = player
        player.setEnemy(self) 
        
    # Set player to Armed
    def armed(self):
        self.hasWeapon = True
        
    # return Bool of if player is armed    
    def isArmed(self):
        return self.hasWeapon
    
    #Set player to Unarmed
    def unarmed(self):
        self.hasWeapon = False    
    
    # Add change to the current mana    
    def changeCurMana(self, change):
        self.curMana = self.curMana + change
        
    # add change to the Total mana
    def changeTotMana(self, change):
        self.totMana = self.totMana + change
        if self.totMana > 10:
            self.totMana = 10
            
        
    # change armor by inc        
    def changeArmor(self, inc):
        output = min(0, self.armor +inc)
        self.armor = max(0, self.armor +inc)
        return output
    
    # Set current mana to total mana
    def startTurn (self):
        self.curMana = self.totMana
    
    # Activate hero power
    def doHeroPower(self):
        if not (self.hp.getTired()):
            self.hp.doPower()
            self.hp.setTired(True)
            
    # Add inc to the life total    
    def incLife(self, inc):
        if self.armor > 0:
            lifeDeduct = self.changeArmor(inc)
            self.life = self.life + lifeDeduct
        else:
            self.life += inc
    
    #Draw a card    
    def draw(self):
        self.hand.draw(self.deck)
     
    #Heal player    
    def heal(self, inc):
        self.life = min(30, self.life + 2)
    
    