from card import *
from cards import *

class Hand:
    def __init__(self):
        self.name = 3
        self.cards = []
        for i in range (10):
            self.cards.append(NULL_CR())
            
    def draw(self, deck):
        i = 0
        while self.cards[i].getName() != "Null" and i < 9:
            print self.cards[i].getName()
            i+=1
            
        if i != 10:
            self.cards[i] = deck.draw()
            
    def getCards(self):
        return self.cards
    
    def setNull(self, pos):
        self.cards[pos] = NULL_CR()
        
    def initialize(self, deck):
        for i in range (7):
            self.cards[i] = deck.draw()
            
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
	self.img = "abusive_sergeant.png"
	
    def isNull(self):
	return True
    