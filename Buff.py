from card import *


class Buff:
    
    def __init__(self):
        self.oneTurn = False
        self.constant = False
        self.growing = False
        
    def getOneTurn(self):
        return self.oneTurn
    
    def setOneTurn(self, boo):
        self.oneTurn = boo
        
    def getConsant(self):
        return self.constant
    
    def setConstant(self, boo):
        self.constant = boo
        
    def getGrowing(self):
        return self.growing
    
    def setGrowing(self, boo):
        self.growing = boo
    