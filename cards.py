from card import *
from random import *
from pygame import *

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
        
    def copy(self):
        return ABU_SRG(self.board, self.screen)
    
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
		drawGrid(self.screen)
		showBoard(self.board.getSpots(), self.screen)
		showHand(self.board.getHands(), self.screen)
		highlight((255, 255, 0), evnt.pos, self.screen)
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
	    
def showBoard(spots, screen):
    for i in range(0,2):
	for j in range(0,6):
	    if (spots[i][j].getOccupied()):
		showCard2(spots[i][j], screen)
		
def showHand(hands, screen):
    for i in range (2):
	for j in range (10):
	    showHandCard(hands[i].getCards()[j], [i,j], screen)
	    
def showCard2(spot, screen):
    nameFont = font.Font(None, 30)
    name = nameFont.render(spot.getCard().getName() , True, (255, 255, 255), BOARD)
    nameRect = name.get_rect()
    nameRect.centerx = spot.getPos()[0] +15
    nameRect.centery = spot.getPos()[1]
    pts = str(spot.getCard().getPower()) + "                  " + str(spot.getCard().getToughness())
    pt = nameFont.render(pts, True, (255, 255, 255), BOARD)
    ptRect = pt.get_rect()
    ptRect.centerx = spot.getPos()[0] + 30
    ptRect.centery = spot.getPos()[1] + 200
    screen.blit(name, nameRect)
    screen.blit(pt, ptRect)
    
def showHandCard(card, pos, screen):
    handFont = font.Font(None, 15)
    if card.getName() != "Null":
	name = handFont.render(card.getName() , True, (255, 255, 255), BOARD)
	nameRect = name.get_rect()
	nameRect.centerx = pos[1]*140 + 70
	nameRect.centery = pos[0]*650 + 20
	
	cost = handFont.render(str(card.getCost()) , True, (255, 255, 255), BOARD)
	costRect = cost.get_rect()
	costRect.centerx = pos[1]*140 + 70
	costRect.centery = pos[0]*650 + 40
	
	screen.blit(name, nameRect)
	screen.blit(cost, costRect)
	
def drawGrid(screen):
    nameFont = font.Font(None, 30)
    draw.rect(screen, BOARD, (0,0,1400,800))
    #Verticals
    for i in range (1,7):
	draw.line(screen, RED, (200*i, 150) , (200*i, 650))
        
    for i in range (1,10):
	draw.line(screen, RED, (140*i, 0) , (140*i, 150))
	draw.line(screen, RED, (140*i, 650) , (140*i, 800))
	
    #Horizontals
    draw.line(screen, RED, (0, 150) , (1400, 150))
    draw.line(screen, RED, (0, 650) , (1400, 650))
    
    draw.rect(screen, (100, 100, 255), (1400,400,150,100))
    name = nameFont.render("End Turn" , True, (155,155,255 ), (100, 100, 0))
    nameRect = name.get_rect()
    nameRect.centerx = 1475 
    nameRect.centery = 450
    screen.blit(name, nameRect)
	
    
