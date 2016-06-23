from copy import *
from random import *

from Deck import *
from Hand import *
from Player import *
from Spot import *
from State import *


#The Board class is responsible for holding the decks, hands, and the 
# current state of the board. 
class Board:
    def __init__(self):
        #spots are the 14 possible spots where you can play a minion
        self.spots = ([],[])
        for i in range (0,7):
            self.spots[0].append(Spot((200*i+70,435)))
            self.spots[1].append(Spot((200*i+70,180)))
        #Hands are each player's hands
        self.hands = (Hand(),Hand())
        
        #Creates two dummy decks, which will be filled in later
        self.Deck1 = Deck("Player1", "Warlock")
        self.Deck2 = Deck("Player2", "Druid")
        
        #Effects begins null, and will hold all of the effects
        self.effects = []
        
        #Initializes the Players with their own decks and placement order
        self.player1 = Player(self.hands[0], self.Deck1, self.spots[0], 0, 0)
        self.player2 = Player(self.hands[1], self.Deck2, self.spots[1], 1, 1)
        
        #Set each player as each others enemy
        self.player1.setEnemies(self.player2)
        #Set the current player
        self.currentPlayer = self.player2
        
    #############################    
    #    Get Statements         #
    #############################        
    def getSpots(self):
        return self.spots
    
    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def getSpot(self,i,j):
        return self.spots[i][j]
    
    def getHands(self):
        return self.hands
    
    def getDecks(self):
        return self.Deck1, self.Deck2
    
    def getEffects(self):
        return self.effects()
    
    def getPlayer1(self):
        return self.player1
    
    def getPlayer2(self):
        return self.player2
    
    
    # SimpleDecks randomly fills two decks with 30 cards from two
    # cardlists. This is primarily used for testing, as it can take
    # a long time to create 30 card decks every time you open the app
    # cards1/cards2 : List of Cards
    # player1/player2: Players 
    def simpleDecks(self, cards1, cards2, player1, player2):
        for i in range (30):
            shuffle(cards1)
            shuffle(cards2)
            newCard1 = cards1[0].copy()
            newCard1.setPlayer(player1)
            newCard2 = cards2[0].copy()
            newCard2.setPlayer(player2)
            newCard1.setState(State(self.hands[0], self.Deck1, self))
            newCard2.setState(State(self.hands[1], self.Deck2, self))
            self.Deck1.insertCard(newCard1)
            self.Deck2.insertCard(newCard2)
        return self.Deck1, self.Deck2
    

    # Adds effect eff to the list of current effects on the board 
    # eff : effect to be added  
    def addEffect(self, eff):
        self.effects.append(eff)
        

    #Triggers all effects that happen when a card is played
    # card: the card that is played
    def playedCreature(self, card):
        for eff in self.effects:
            eff.playCreature(card)
    
    #Triggers all effects that happen when a card dies
    # card: the card that died        
    def cardDeath(self, card):
        for eff in self.effects:
            eff.killCreature(card)
            
    #  Switches who's turn it is
    def switchCurrent(self):
        self.currentPlayer = self.currentPlayer.getEnemy()
        
        

        