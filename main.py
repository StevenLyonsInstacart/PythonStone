#Main  HS game
from pygame import *
from card import *
from Grid import *
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BOARD = (205,182,139)


def check_to_quit():
    for evnt in event.get(): # checks all events that happen
        keys = key.get_pressed()
        keyz= key.get_pressed ()
        if evnt.type == QUIT:
            return False
    return True

def drawGrid(screen):
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
	    
def showCard(gridSpot, card):
    name = nameFont.render(card.getName() , True, (255, 255, 255), BOARD)
    nameRect = name.get_rect()
    nameRect.centerx = gridSpot[0] * 200 + 40
    nameRect.centery = 400 + 40
    pts = str(card.getPower()) + "                  " + str(card.getToughness())
    pt = nameFont.render(pts, True, (255, 255, 255), BOARD)
    ptRect = pt.get_rect()
    ptRect.centerx = gridSpot[0] * 200 + 100
    ptRect.centery = 620
    screen.blit(name, nameRect)
    screen.blit(pt, ptRect)
    
def playCard(gridSpot, card, board):
    spots = board.getSpots()
    updateSpot = spots[gridSpot[0]][gridSpot[1]]
    updateSpot.setCard(card)
    updateSpot.setOccupied(True)
    
def showCard2(spot):
    name = nameFont.render(spot.getCard().getName() , True, (255, 255, 255), BOARD)
    nameRect = name.get_rect()
    nameRect.centerx = spot.getPos()[0] - 20
    nameRect.centery = spot.getPos()[1]
    pts = str(spot.getCard().getPower()) + "                  " + str(spot.getCard().getToughness())
    pt = nameFont.render(pts, True, (255, 255, 255), BOARD)
    ptRect = pt.get_rect()
    ptRect.centerx = spot.getPos()[0] + 30
    ptRect.centery = spot.getPos()[1] + 200
    screen.blit(name, nameRect)
    screen.blit(pt, ptRect)
    
def showHandCard(card, pos):
    if card.getName() != "Null":
	name = nameFont.render(card.getName() , True, (255, 255, 255), BOARD)
	nameRect = name.get_rect()
	nameRect.centerx = pos[1]*140 + 40
	nameRect.centery = pos[0]*650 + 20
	
	cost = nameFont.render(str(card.getCost()) , True, (255, 255, 255), BOARD)
	costRect = cost.get_rect()
	costRect.centerx = pos[1]*140 + 40
	costRect.centery = pos[0]*650 + 40
	
	screen.blit(name, nameRect)
	screen.blit(cost, costRect)
    
def showBoard(spots):
    for i in range(0,2):
	for j in range(0,6):
	    if (spots[i][j].getOccupied()):
		showCard2(spots[i][j])
		
def showHand(hands):
    for i in range (2):
	for j in range (10):
	    showHandCard(hands[i].getCards()[j], [i,j])
		
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
			return spots[reversei][j], [i*250 + 150, j*200, 200, 250], "B"
	    for j in range(0,10):
		if 140*j < mx < 140*(j+1) and 0 < my < 150 :
		    square = [i,j]
		    print j, i
		    
		    return [hands[0].getCards()[j], [0,j]], [0, j*140, 140, 150], "H"
		
	    for j in range(0,10):
		if 140*j < mx < 140*(j+1) and 650 < my < 800 :
		    square = [i,j]
		    print j, i
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
		    else:
			print i, j, "WASSSUP"
			print type(current[0].getPower()), state
			spots[i][j].setCard(current[0])
			spots[i][j].setOccupied(True)
			hands[current[1][0]].setNull(current[1][1])
			current = None
			state = None
    return current, [i,j, 200, 250], state
    
init()    
size =(1400,800)
screen= display.set_mode (size)
nameFont = font.Font(None, 30)
selected = None
square = None
display.flip()
breaker = True
grid = Grid()
board = grid.getBoard()
spots = board.getSpots()
hands = board.getHands()
yeti = Creature("YETI", 4, 4, 5)
beti = Creature("YETI", 4, 3, 5)
shrek = Creature("YETI", 4, 2, 5)
state = None
x = 0
playCard((1,5), yeti, board)
playCard((1,0), shrek, board)
playCard((0,0), beti, board)
while (breaker and x < 5):
    x = x + 0.02
    breaker = check_to_quit()
    drawGrid(screen)
    highlight(mouse.get_pos(), screen, selected, square)


    showBoard(spots)
    showHand(hands)
    newEvent = event.wait()
    if newEvent.type == MOUSEBUTTONDOWN:
	print type(selected)
	selected, square, state = select(newEvent, spots, selected, state, hands)
	
    else:
	breaker = check_to_quit()
    display.flip()
quit()