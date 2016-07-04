#Spot is a space on the Board which can hold a card
class Spot:
    def __init__(self, pos):
        self.occupied = False
        self.card = None 
        self.pos = pos
        
    def getOccupied(self):
        return self.occupied
    
    def setOccupied(self,boo):
        self.occupied = boo
        
    def getCard(self):
        return self.card
    
    def setCard(self,newCard):
        self.card = newCard
        
    def getPos(self):
        return self.pos
    
    def setPos(self,newPos):
        self.pos = newPos
        
        
    def getType(self):
        return "Spot"
    