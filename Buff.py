from card import *

# The Buff class represents Buffs that can be on minions.

class Buff:
    
    def __init__(self):
        self.oneTurn = False
        self.constant = False
        self.growing = False
        
    ######################
    #    Get Statements  #
    ######################
    def getOneTurn(self):
        return self.oneTurn
    
    def getGrowing(self):
        return self.growing
    
    def getConsant(self):
        return self.constant
    
    ######################
    #    Set Statements  #
    ######################
    
    def setOneTurn(self, boo):
        self.oneTurn = boo
        
    def setConstant(self, boo):
        self.constant = boo
        
    def setGrowing(self, boo):
        self.growing = boo
    