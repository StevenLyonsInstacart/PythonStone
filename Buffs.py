from Buff import *
class ABU_BUFF(Buff):
    
    def __init__(self, creature):
        self.oneTurn = True
        self.constant = False
        self.growing = False
        self.host = creature
        
    def applyBuff(self):
        self.host.setPower(self.host.getPower() + 2)
        
    def removeBuff(self):
        self.host.setPower(self.host.getPower() - 2)
        
    def setCreature(self, creature):
        self.host = creature
        
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
        