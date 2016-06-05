from card import *
from random import *
from pygame import *
from Buffs import *
from Buff import *
from DrawBoard import *

RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BOARD = (205,182,139)


#handFont = font.Font(None, 15)

class NULL_CREATURE(Creature):
    def __init__(self):
        self.name = "Null"
        self.power = 0
        self.toughness = 0
        self.cost = 0
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
	self.buffs = []
    
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
        self.buffs = []
	
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
	self.buffs = []
        
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
        self.buffs = []
	
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
	self.buffs = []
        
    def copy(self):
        return MUR_RAID()
    
    def getClass(self):
        return self.classType
    
class ABU_SRG(Creature):
    
    def __init__(self, board, screen):
        self.name = "Abusive Sergeant"
        self.power = 2
        self.toughness = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
        
    def copy(self):
        return ABU_SRG(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    def battleCry(self):
	selectedBattleCry(ABU_BUFF(None), self.board, self.screen)
	
class LNC_CAR(Creature):
    
    def __init__(self, board, screen):
        self.name = "Lance Carrier"
        self.power = 1
        self.toughness = 2
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
        
    def copy(self):
        return ABU_SRG(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    def battleCry(self):
	selectedBattleCry(LNC_BUFF(None), self.board, self.screen)
	
class IRN_OWL(Creature):
    
    def __init__(self, board, screen):
        self.name = "Iron Beak Owl"
        self.power = 2
        self.toughness = 1
        self.cost = 3
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
        
    def copy(self):
        return IRN_OWL(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    def battleCry(self):
	selectedBattleCry(OWL_BUFF(None), self.board, self.screen)
        
def selectedBattleCry(buff, board, screen):	
    waiting = True
    spots = board.getSpots()
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
			    buff.setCreature(spots[reversei][j].getCard())
			    spots[reversei][j].getCard().addBuff(buff)
			    buff.applyBuff()
			    waiting = False
	    drawGrid(screen)
	    showBoard(board.getSpots(), screen)
	    showHand(board.getHands(), screen)
	    highlight((255, 255, 0), evnt.pos, screen)
	    display.flip()

def highlight(colour, pos, screen):
    for i in range (0,10):
	if pos[1] < 150 and pos[0]> i*140 and pos[0] < (i+1)*140:
	    xcor = pos[0] % 140
	    draw.rect(screen, colour, (140*i,0, 140, 150), 10)
	if pos[1] > 650 and pos[0]> i*140 and pos[0] < (i+1)*140:
	    xcor = pos[0] % 140
	    draw.rect(screen, colour, (140*i,650, 140, 150), 10)
    for i in range (0,7):
	if pos[1] > 150 and pos[1] < 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
	    draw.rect(screen, colour, (200*i,150, 200, 250), 10)
	if pos[1] < 650 and pos[1] > 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
	    draw.rect(screen, colour, (200*i,400, 200, 250), 10)
	    

    
