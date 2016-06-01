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
        