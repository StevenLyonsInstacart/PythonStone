from Buff import *
from Constants import *

#Buff generated by Abusive Sergeant, which is +2 attack until end of turn
class ABU_BUFF(Buff):
    
    def __init__(self, creature):
        self.oneTurn = True
        self.constant = False
        self.growing = False
        self.host = creature
        
    #Plus two Attack
    def applyBuff(self):
        self.host.setPower(self.host.getPower() + 2)
        
    #Removes the additional Attack
    def removeBuff(self):
        self.host.setPower(self.host.getPower() - 2)
        
    def setCreature(self, creature):
        self.host = creature
        

#Lance Carrier Buff, which is a permanent +2 attack    
class LNC_BUFF(Buff):
    
    def __init__(self, creature):
        self.oneTurn = False
        self.constant = True
        self.growing = False
        self.host = creature
        
    def applyBuff(self):
        self.host.setPower(self.host.getPower() + 2)
        
    def removeBuff(self):
        self.host.setPower(self.host.getPower() - 2)
        
    def setCreature(self, creature):
        self.host = creature
        
        
    # OWL_BUFF is actually a targeted silence, ala ironbeak owl
class OWL_BUFF(Buff):
    
    def __init__(self, creature):
        self.oneTurn = False
        self.constant = True
        self.growing = False
        self.host = creature
        
    def applyBuff(self):
        self.host.clearBuffs()
        
    def removeBuff(self):
        pass
        
    def setCreature(self, creature):
        self.host = creature
        
    
#Grimscale Oracle Buff, plus one attack to each other Murloc    
class GRM_BUFF(Buff):
    
    def __init__(self, creature, board):
        self.oneTurn = False
        self.constant = True
        self.growing = False
        self.host = creature
        self.board = board
        
    def applyBuff(self):
        self.host.setPower(self.host.getPower() + 1)
    def removeBuff(self):
        self.host.setPower(self.host.getPower() - 1)
        
    def setCreature(self, creature):
        self.host = creature
        
#Sstormwind Champion Buff, +1/+1 to each minion    
class CHMP_BUFF(Buff):
    
    def __init__(self, creature, board):
        self.oneTurn = False
        self.constant = True
        self.growing = False
        self.host = creature
        self.board = board
        
    def applyBuff(self):
        self.host.setPower(self.host.getPower() + 1)
        self.host.setToughness(self.host.getToughness() + 1)
    def removeBuff(self):
        self.host.setPower(self.host.getPower() - 1)
        self.host.setToughness(self.host.getToughness() - 1)
        
    def setCreature(self, creature):
        self.host = creature
        
#Shattered Sun Cleric Buff, give one minion +1/+1        
class SUN_BUFF(Buff):
    
    def __init__(self, creature):
        self.oneTurn = False
        self.constant = True
        self.growing = False
        self.host = creature
        self.board = getBoard()
        
    def applyBuff(self):
        self.host.setPower(self.host.getPower() + 1)
        self.host.setToughness(self.host.getToughness() + 1)
    def removeBuff(self):
        self.host.setPower(self.host.getPower() - 1)
        self.host.setToughness(self.host.getToughness() - 1)
        
    def setCreature(self, creature):
        self.host = creature
        