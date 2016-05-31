from Spot import *
from Hand import *
class Board:
    def __init__(self):
        self.spots = ([],[])
        for i in range (0,7):
            self.spots[0].append(Spot((200*i+70,435)))
            self.spots[1].append(Spot((200*i+70,180)))
        self.hands = (Hand(),Hand())
        
            
    def getSpots(self):
        return self.spots
    
    def getSpot(self,i,j):
        return self.spots[i][j]
    
    def getHands(self):
        return self.hands