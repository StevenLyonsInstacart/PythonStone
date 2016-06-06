from Spot import *
from Hand import *
from Deck import *
from copy import *
from State import *
import random
class Board:
    def __init__(self):
        self.spots = ([],[])
        for i in range (0,7):
            self.spots[0].append(Spot((200*i+70,435)))
            self.spots[1].append(Spot((200*i+70,180)))
        self.hands = (Hand(),Hand())
        self.Deck1 = Deck("Player1", "Warlock")
        self.Deck2 = Deck("Player2", "Druid")
        self.curMana1 = 0
        self.curMana2 = 0
        self.totMana1 = 0
        self.totMana2 = 0
            
    def getSpots(self):
        return self.spots
    
    def getSpot(self,i,j):
        return self.spots[i][j]
    
    def getHands(self):
        return self.hands
    
    def simpleDecks(self, cards1, cards2):
        for i in range (30):
            random.shuffle(cards1)
            random.shuffle(cards2)
            newCard1 = cards1[0].copy()
            newCard2 = cards2[0].copy()
            newCard1.setState(State(self.hands[0], self.Deck1, self))
            newCard2.setState(State(self.hands[1], self.Deck2, self))
            self.Deck1.insertCard(newCard1)
            self.Deck2.insertCard(newCard2)
        return self.Deck1, self.Deck2
    
    def getDecks(self):
        return self.Deck1, self.Deck2
    
    def getTotalMana1(self):
        return self.totMana1
    def getTotalMana2(self):
        return self.totMana2
    def getCurMana1(self):
        return self.curMana1
    def getCurMana2(self):
        return self.curMana2
    
    def changeCurMana1(self, change):
        self.curMana1 = self.curMana1 + change
        
    def changeCurMana2(self, change):
        self.curMana2 = self.curMana2 + change
        
    def changeTotMana1(self, change):
        self.totMana1 = self.totMana1 + change
        if self.totMana1 > 10:
            self.totMana1 = 10
        
    def changeTotMana2(self, change):
        self.totMana2 = self.totMana2 + change
        if self.totMana2 > 10:
            self.totMana2 = 10
            
    def player1Turn (self):
        self.curMana1 = self.totMana1
        
    def player2Turn (self):
        self.curMana2 = self.totMana2

        