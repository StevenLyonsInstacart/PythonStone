from Board import *
from Deck import *
from Hand import *
from Spot import *

class State:
    
    def __init__(self, Hand, Deck, Board):
        self.hand = Hand
        self.deck = Deck
        self.board = Board
        
    def getHand(self):
        return self.hand
    
    def getDeck(self):
        return self.deck
    
    def getBoard(self):
        return self.board