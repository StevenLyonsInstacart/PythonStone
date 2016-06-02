from card import *
from random import *
from pygame import *

class NULL_CREATURE(Creature):
    def __init__(self):
        self.name = "Null"
        self.power = 0
        self.toughness = 0
        self.cost = 0
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
    
class CH_YETI(Creature):
    def __init__(self):
        self.name = "Chillwind Yeti"
        self.power = 4
        self.toughness = 5
        self.cost = 4
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        self.owner = 0
        self.tired = True
        
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
        self.owner = 0
        self.tired = True
        
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
        self.owner = 0
        self.tired = True
        
    def getClass(self):
        return self.classType
    
    def copy(self):
        return FL_JUG()
        
    def hasBattleCry(self):
        return True
    
class MUR_RAID(Creature):
    
    def __init__(self):
        self.name = "Murloc Raider"
        self.power = 2
        self.toughness = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = "Murloc"
        self.owner = 0
        self.tired = True
        
    def copy(self):
        return MUR_RAID()
    
    def getClass(self):
        return self.classType
    
class ABU_SRG(Creature):
    
    def __init__(self, board):
        self.name = "Abusive Sergeant"
        self.power = 2
        self.toughness = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
        
    def copy(self):
        return ABU_SRG(self.board)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    def battleCry(self):
	
        waiting = True
	spots = self.board.getSpots()
        while waiting:
	    for evnt in event.get():
		if evnt.type == MOUSEBUTTONDOWN:
		    mx, my = evnt.pos
		    i = 1
		    for j in range(0,7):
			if 200*j < mx < 200*(j+1) and 150 + 250*(i) < my < 150 + 250*(i+1):
			    square = [i,j]
			    reversei = abs(1-i)
			    if spots[reversei][j].getOccupied():
				    spots[reversei][j].getCard().setPower(spots[reversei][j].getCard().getPower() + 2)
				    waiting = False
    
