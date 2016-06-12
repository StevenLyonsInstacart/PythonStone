from card import *
from random import *
from pygame import *
from Buffs import *
from Buff import *
from DrawBoard import *
from Damage import *
from Effect import *
from Effects import *

class Player:
    
    def __init__(self, hand, deck, spots, role="None"):
        self.hand = hand
        self.deck = deck
        self.spots = spots
        self.role = role
        self.portrait = "guldan_portrait.jpg"
        self.life = 30
        
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
    
    def setHand(self, hand):
        self.hand = hand
    def setDeck(self, deck):
        self.deck = deck
    def setSpots(self, spots):
        self.spots = spots
    def setRole(self, role):
        self.role = role
    def setLife(self, life):
        self.life = life
        
    
    def incLife(self, inc):
        self.life += inc
    
    