from Spot import *
from Hand import *
from Deck import *
from copy import *
from State import *
from Player import *
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
        self.effects = []
        
        self.player1 = Player(self.hands[0], self.Deck1, self.spots[0], 0, 0)
        self.player2 = Player(self.hands[1], self.Deck2, self.spots[1], 1, 1)
        
        
        self.player1.setEnemies(self.player2)
        self.currentPlayer = self.player1
            
    def getSpots(self):
        return self.spots
    
    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def getSpot(self,i,j):
        return self.spots[i][j]
    
    def getHands(self):
        return self.hands
    
    def simpleDecks(self, cards1, cards2, player1, player2):
        for i in range (30):
            random.shuffle(cards1)
            random.shuffle(cards2)
            newCard1 = cards1[0].copy()
            newCard1.setPlayer(player1)
            newCard2 = cards2[0].copy()
            newCard2.setPlayer(player2)
            newCard1.setState(State(self.hands[0], self.Deck1, self))
            newCard2.setState(State(self.hands[1], self.Deck2, self))
            self.Deck1.insertCard(newCard1)
            self.Deck2.insertCard(newCard2)
        return self.Deck1, self.Deck2
    
    def getDecks(self):
        return self.Deck1, self.Deck2
        
    def addEffect(self, eff):
        self.effects.append(eff)
        
    def getEffects(self):
        return self.effects()
    
    def playedCreature(self, card):
        for eff in self.effects:
            eff.playCreature(card)
            
    def cardDeath(self, card):
        for eff in self.effects:
            eff.killCreature(card)
            
    def getPlayer1(self):
        return self.player1
    
    def getPlayer2(self):
        return self.player2
    def switchCurrent(self):
        self.currentPlayer = self.currentPlayer.getEnemy()
        

        