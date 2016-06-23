from pygame import *
from random import *

from Buff import *
from Buffs import *
from Damage import *
from DrawBoard import *
from Effect import *
from Effects import *
from card import *

#Colours
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BOARD = (205,182,139)



#Null Creature is an empty creature that wont be shown on screen.
#Currently Null_Creature is used in empty board and hand spaces
class NULL_CREATURE(Creature):
    def __init__(self):
        self.name = "Null"
        self.power = 0
        self.toughness = 0
	self.maxHealth = 0
        self.cost = 0
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
	self.buffs = []
	self.img = "abusive_sergeant.png"
    
    
#Representation of Chillwind Yeti    
class CH_YETI(Creature):
    def __init__(self):
        self.name = "Chillwind Yeti"
        self.power = 4
        self.toughness = 5
	self.maxHealth = 5
        self.cost = 4
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
	self.img = "chillwind_yeti.png"
	
    def getClass(self):
        return self.classType
    
    def copy(self):
        return CH_YETI()
    
#Representation of River Crocolisk    
class RIV_CROC(Creature):
    def __init__(self):
        self.name = "River Crocolisk"
        self.power = 2
        self.toughness = 3
	self.maxHealth = 3
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = "Beast"
        self.battleCry = None
        self.owner = 0
        self.tired = True
	self.buffs = []
	self.img = "river_crocolisk.png"
	
        
    def getClass(self):
        return self.classType
    def copy(self):
        return RIV_CROC()

#Representation of Flame Juggler    
class FL_JUG(Creature):
    
    #BattleCry: deal 1 damage to a random enemy
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
	self.maxHealth = 3
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.buffs = []
	self.img = "flame_juggler.png"
	
    def getClass(self):
        return self.classType
    
    def copy(self):
        return FL_JUG()
    #Has a battlecry    
    def hasBattleCry(self):
        return True

#Representation of Murloc Raider    
class MUR_RAID(Creature):
    
    def __init__(self):
        self.name = "Murloc Raider"
        self.power = 2
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = "Murloc"
        self.owner = 0
        self.tired = True
	self.buffs = []
	self.img = "murloc_raider.png"
        
    def copy(self):
        return MUR_RAID()
    
    def getClass(self):
        return self.classType
    
#Representation of Grimscale Oracle    
class GRM_MUR(Creature):
    
    def __init__(self, board, screen):
        self.name = "Grimscale Oracle"
        self.power = 1
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = "Murloc"
        self.owner = 0
        self.tired = True
	self.board = board
	self.screen = screen
	self.buffs = []
	self.effects = [GRM_EFF(board, self)]
	self.img = "grimscale_oracle.png"
        
    def copy(self):
        return GRM_MUR(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasEffect(self):
	return True
    
    #Buff all other murlocs with +1 attack
    def doEffect(self):
	self.board.addEffect(self.effects[0])
	self.effects[0].onPlay()
    
#Representation of Abusive Sergeant    
class ABU_SRG(Creature):
    
    def __init__(self, board, screen):
        self.name = "Abusive Sergeant"
        self.power = 2
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
	self.effects = []
	self.img = "abusive_sergeant.png"
        
    def copy(self):
        return ABU_SRG(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    #Give a minion +2 attack until end of turn
    def battleCry(self):
	selectedBattleCry(ABU_BUFF(None), self.board, self.screen, self.img)

#Lance Carrier Representation	
class LNC_CAR(Creature):
    
    def __init__(self, board, screen):
        self.name = "Lance Carrier"
        self.power = 1
        self.toughness = 2
	self.maxHealth = 2
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
	self.img = "lance_carrier.png"
        
    def copy(self):
        return ABU_SRG(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    #Ggive a minion +2 attack permanently
    def battleCry(self):
	selectedBattleCry(LNC_BUFF(None), self.board, self.screen, self.img)
	
#Representation of IronBeak Owl    
class IRN_OWL(Creature):
    
    def __init__(self, board, screen):
        self.name = "Iron Beak Owl"
        self.power = 2
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 3
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
	self.img = "ironbeak_owl.png"
        
    def copy(self):
        return IRN_OWL(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    #Silence a Creature
    def battleCry(self):
	selectedBattleCry(OWL_BUFF(None), self.board, self.screen, self.img)

#Representation of Novice Engineer	
class NOV_ENG(Creature):
    
    def __init__(self, board, screen):
        self.name = "Novice Engineer"
        self.power = 1
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
	self.img = "novice_engineer.png"
        
    def copy(self):
        return NOV_ENG(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    #Draw a card
    def battleCry(self):
	player = self.getPlayer()
	player.getHand().draw(player.getDeck())

#Representation of Silver Hand Recruit	
class DUDE(Creature):
    
    def __init__(self):
        self.name = "SilverHand recruit"
        self.power = 1
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
	self.buffs = []
	self.img = "silverhand_recruit.png"
        
    def copy(self):
        return DUDE()
    
    def getClass(self):
        return self.classType
    
#Rrepresentation of Loot Hoarder	
class LOT_HRD(Creature):
    
    def __init__(self, board, screen):
        self.name = "Loot Hoarder"
        self.power = 2
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
	self.img = "loot_hoarder.png"
        
    def copy(self):
        return LOT_HRD(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasDeathRattle(self):
        return True
    
    #Draw a card on Death
    def deathRattle(self):
	       player = self.getPlayer()
	       player.getHand().draw(player.getDeck())

#Representation of Elven Archer	
class ELF_ARC(Creature):
    
    def __init__(self, board, screen):
        self.name = "Elvish Archer"
        self.power = 1
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = board
	self.screen = screen
	self.buffs = []
	self.img = "elven_archer.png"
        
    def copy(self):
        return ELF_ARC(self.board, self.screen)
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    #Deal 1 Damage
    def battleCry(self):
	target = selectCard(self.board, self.screen, self.img)
	dealDamage(target, 1, self.board)

#A helper function that will return the spot of a selected card.	
def selectCard(board, screen, filename):	
    waiting = True
    spots = board.getSpots()
    while waiting:
	
    	for evnt in event.get():
    	    
    	    if evnt.type == MOUSEBUTTONDOWN:
    		mx, my = evnt.pos
            #i represents the side of the board
    		for i in range (2):
                #j represents the index of the spot
    		    for j in range(0,7):
    			     if 200*j < mx < 200*(j+1) and 150 + 250*(i) < my < 150 + 250*(i+1):
    			         square = [i,j]
    			         reversei = abs(1-i)
                         #Exit when clicked on a spot with a card in it
    			         if spots[reversei][j].getOccupied():
    				        return spots[reversei][j]
    	    drawGrid(screen, board, filename)
    	    showBoard(board.getSpots(), screen)
    	    showHand(board.getHands(), screen, 1)
    	    highlight((255, 255, 0), evnt.pos, screen)
    	    display.flip()

#Apply a buff to a card currently on the fiels
def selectedBattleCry(buff, board, screen, filename):	
    waiting = True
    spots = board.getSpots()
    while waiting:
	
	for evnt in event.get():
	    
	    if evnt.type == MOUSEBUTTONDOWN:
		mx, my = evnt.pos
		for i in range (2):
		    for j in range(0,7):
			if 200*j < mx < 200*(j+1) and 150 + 250*(i) < my < 150 + 250*(i+1):
			    square = [i,j]
			    reversei = abs(1-i)
			    if spots[reversei][j].getOccupied():
				buff.setCreature(spots[reversei][j].getCard())
				spots[reversei][j].getCard().addBuff(buff)
				buff.applyBuff()
				waiting = False
	    drawGrid(screen, board, filename)
	    showBoard(board.getSpots(), screen)
	    showHand(board.getHands(), screen, 1)
	    highlight((255, 255, 0), evnt.pos, screen)
	    display.flip()
	    

#While selecting a battle cry, highlight wherever the mouse is
def highlight(colour, pos, screen):
    for i in range (0,10):
	if pos[1] < 100 and pos[0]> i*140 and pos[0] < (i+1)*140:
	    xcor = pos[0] % 140
	    draw.rect(screen, colour, (140*i,0, 140, 100), 10)
	if pos[1] > 700 and pos[0]> i*140 and pos[0] < (i+1)*140:
	    xcor = pos[0] % 140
	    draw.rect(screen, colour, (140*i,700, 140, 100), 10)
    for i in range (0,7):
	if pos[1] > 200 and pos[1] < 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
	    draw.rect(screen, colour, (200*i,200, 200, 200), 10)
	if pos[1] < 600 and pos[1] > 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
	    draw.rect(screen, colour, (200*i,400, 200, 200), 10)
	    

    
