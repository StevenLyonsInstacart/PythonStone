#Main  HS game
#To Lindsay
from pygame import *
from card import *
from Grid import *
from cards import *
from random import *
from Turn import *
from DrawBoard import *

RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BOARD = (205,182,139)
LINDSAY = (255, 7, 162)
#BOARD = LINDSAY
turn = 0

def check_to_quit():
    for evnt in event.get(): # checks all events that happen
        keys = key.get_pressed()
        keyz= key.get_pressed ()
        if evnt.type == QUIT:
            return False
    return True



def checkExit(mouse):
    mx, my = mouse.pos
    if 1000 < mx < 1200 and 600 < my < 670:
	return False
    return  True

def addCard(pos, cards):
    for i in range (7):
	if 400 < pos[0] < 650 and 80+50*i < pos[1] < 80+(50*(i+1)):
	    return cards[i].copy()
    return None
    
    
def highlight(pos, screen, selcted, square):
    for i in range (0,10):
	if pos[1] < 150 and pos[0]> i*140 and pos[0] < (i+1)*140:
	    xcor = pos[0] % 140
	    draw.rect(screen, GREEN, (140*i,0, 140, 150), 10)
	if pos[1] > 650 and pos[0]> i*140 and pos[0] < (i+1)*140:
	    xcor = pos[0] % 140
	    draw.rect(screen, GREEN, (140*i,650, 140, 150), 10)
    for i in range (0,7):
	if pos[1] > 150 and pos[1] < 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
	    draw.rect(screen, GREEN, (200*i,150, 200, 250), 10)
	if pos[1] < 650 and pos[1] > 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
	    draw.rect(screen, GREEN, (200*i,400, 200, 250), 10)
    if selected != None:
	square0 = abs(1-square[0])
	draw.rect(screen, (0,255,255), (square[1], square0, square[2], square[3]), 10)
	    
    
def playCard(gridSpot, card, board):
    spots = board.getSpots()
    updateSpot = spots[gridSpot[0]][gridSpot[1]]
    updateSpot.setCard(card)
    updateSpot.setOccupied(True)
    
		
def fight (spot1, spot2):
    print "fight!"
    attacker = spot1.getCard()
    defender = spot2.getCard()
    nh1 = attacker.getToughness() - defender.getPower()
    nh2 = defender.getToughness() - attacker.getPower()
    attacker.setToughness(nh1)
    defender.setToughness(nh2)
    print attacker.getToughness()
    if attacker.getToughness() < 1:
	print "A"
	spot1.setCard(None)
	spot1.setOccupied(False)
    if defender.getToughness() < 1:
	print "B"
	spot2.setCard(None)
	spot2.setOccupied(False)
	
		
def select(mouseObj, spots, current, state, hands):
    if current  == None:
	mx, my = mouseObj.pos
	for i in range (0,2):
	    for j in range(0,7):
		if 200*j < mx < 200*(j+1) and 150 + 250*(i) < my < 150 + 250*(i+1):
		    square = [i,j]
		    reversei = abs(1-i)
		    if spots[reversei][j].getOccupied():
			if spots[reversei][j].getCard().getTired() == False:
			    return spots[reversei][j], [i*250 + 150, j*200, 200, 250], "B"
	    for j in range(0,10):
		if 140*j < mx < 140*(j+1) and 0 < my < 150 :
		    square = [i,j]
		    print j, i
		    if turn == 1:
			return [hands[0].getCards()[j], [0,j]], [0, j*140, 140, 150], "H"
		
	    for j in range(0,10):
		if 140*j < mx < 140*(j+1) and 650 < my < 800 :
		    square = [i,j]
		    print j, i
		    if turn == 0:
			return [hands[1].getCards()[j], [1,j]], [650, j*140, 140, 150], "H"
		
    else:
	mx, my = mouseObj.pos
	for i in range (0,2):
	    for j in range(0,7):
		if 200*j < mx < 200*(j+1) and 150 + 250*(i) < my < 150 + 250*(i+1):
		    i = abs(1-i)
		    if state == "B":
			
			
			fight(spots[i][j], current)
			current = None
			state = None
			
		    #Play Card
		    else:
			mana = [board.getCurMana1(), board.getCurMana2()]
			if mana[abs(turn - 1)] >= current[0].getCost():
			    if turn == 1:
				board.changeCurMana1(-current[0].getCost())
			    else:
				board.changeCurMana2(-current[0].getCost())
			    spots[i][j].setCard(current[0])
			    spots[i][j].setOccupied(True)
			    hands[current[1][0]].setNull(current[1][1])
			    showBoard(spots, screen)
			    display.flip()
			    if current[0].hasBattleCry():
				current[0].battleCry()
			    current = None
			    state = None
			else:
			    return None, None, None
    return current, [i,j, 200, 250], state
    
init()    
size =(1600,800)
screen= display.set_mode (size)
nameFont = font.Font(None, 30)
handFont = font.Font(None, 15)
selected = None
square = None
display.flip()
breaker = True
grid = Grid()
board = grid.getBoard()
spots = board.getSpots()
hands = board.getHands()


twice = 0

state = None
x = 0
selecting = True
cardList = [CH_YETI(), FL_JUG(), RIV_CROC(), MUR_RAID(), ABU_SRG(board, screen), LNC_CAR(board, screen), IRN_OWL(board, screen)]
deck1Cards = []
deck2Cards = []
while (selecting):
    showSelect(screen, cardList, 1, (255,255,255))
    for evnt in event.get():
	if evnt.type == MOUSEBUTTONDOWN:
	    selecting = checkExit(evnt)
	    newCard = addCard(evnt.pos, cardList)
	    if newCard:
		deck1Cards.append(newCard)
	elif evnt.type == QUIT:
	    quit()
    display.flip()
selecting = True 

while (selecting):
    showSelect(screen, cardList, 1, (200, 200, 200))
    for evnt in event.get():
	if evnt.type == MOUSEBUTTONDOWN:
	    selecting = checkExit(evnt)
	    newCard = addCard(evnt.pos, cardList)
	    if newCard:
		deck2Cards.append(newCard)
    display.flip()

deck1, deck2 = board.simpleDecks(deck1Cards,deck2Cards)
hands[0].initialize(deck1)
hands[1].initialize(deck2)    
    
while (breaker):
    breaker = check_to_quit()
    drawGrid(screen, board)
    highlight(mouse.get_pos(), screen, selected, square)


    showBoard(spots, screen)
    showHand(hands, screen)
    time.wait(10)
    for newEvent in event.get():
	if newEvent.type == MOUSEBUTTONDOWN:
	    
	    selected, square, state = select(newEvent, spots, selected, state, hands)
	    turn = endTurn(newEvent.pos, turn, board)
	    print turn, "YOOO"
	else:
	    if newEvent.type == QUIT: 
		breaker = False
    display.flip()
quit()