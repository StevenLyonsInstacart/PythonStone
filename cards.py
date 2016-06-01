from card import *
from random import *
class CH_YETI(Creature):
    def __init__(self):
        self.name = "Chillwind Yeti"
        self.power = 4
        self.toughness = 5
        self.cost = 4
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        
    def getClass(self):
        return self.classType
    
    def copy(self):
        return CH_YETI()
    
class RIV_CROC(Creature):
    def __init__(self):
        self.name = "River Crocolisk"
        self.power = 2
        self.toughness = 3
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = "Beast"
        self.battleCry = None
        
    def getClass(self):
        return self.classType
    def copy(self):
        return RIV_CROC()
    
class FL_JUG(Creature):
    
    def battleCry(self):
        curBoard = self.state.getBoard()
        enemySide = curBoard.getSpots()[1]
        sanity = 0
        check = int(random()*7)
        while (enemySide[check].getOccupied() == False and sanity<100):
            sanity += 1
            check = int(random()*7)
        if sanity < 100:
            card = enemySide[check].getCard()
            card.ping()
            
        
        
    def __init__(self):
        self.name = "Flame Juggler"
        self.power = 2
        self.toughness = 3
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        
    def getClass(self):
        return self.classType
    
    def copy(self):
        return FL_JUG()
        
    def hasBattleCry(self):
        return True