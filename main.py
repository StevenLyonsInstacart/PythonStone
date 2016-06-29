#Main  HS game
#To Lindsay
from pygame import *
import random

from Board import *
from Damage import *
from DrawBoard import *
from Turn import *
from card import *
from cards import *
from heroPower import *
from spawn import *
from Constants import *
from Messages import *
from Generator import *
from selectionScreen import *
from hover import *
from inputbox import *


#Colour Declerations
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BOARD = (205,182,139)
LINDSAY = (255, 7, 162)
#BOARD = LINDSAY

# Turn tracker
turn = 0
# Get foldername from Constants
foldername = getFoldername()

#Number of cards show at a time on card selection screen
DISPLAYNUM = 4

#filename to be hovered over
filename = foldername+"abusive_sergeant.png"


#Check to see if User wants to quit the application
def check_to_quit():
		for evnt in event.get(): # checks all events that happen
				keys = key.get_pressed()
				keyz= key.get_pressed ()
				if evnt.type == QUIT:
						return False
		return True



#Check if a Player has clicked on their hero power
def checkHeroPower(pos, turn):
		if turn  == 1:
			if 19*widthInc < pos[0] < 21*widthInc and 2*heightInc < pos[1] < 4*heightInc:
					player1.doHeroPower()
		else:
			if 19*widthInc < pos[0] < 21*widthInc and 12*heightInc < pos[1] < 14*heightInc:
					player2.doHeroPower()



# Highlight the current space hovered over and the last space clicked
def highlight(pos, screen, selcted, square):

    
    for i in range (0,10):
        if pos[1] < heightInc*2  and pos[0]> i*tenth and pos[0] < (i+1)*tenth:
            xcor = pos[0] % tenth
            draw.rect(screen, GREEN, (tenth*i,0, tenth, heightInc*2), 10)
        if pos[1] > heightInc*14 and pos[0]> i*tenth and pos[0] < (i+1)*tenth:
            xcor = pos[0] % tenth
            draw.rect(screen, GREEN, (tenth*i,heightInc*14, tenth, heightInc*2), 10)
    for i in range (0,7):
        if pos[1] > heightInc*4 and pos[1] < heightInc*8 and pos[0]> i*widthInc*4 and pos[0] < (i+1)*widthInc*4:
			draw.rect(screen, GREEN, (widthInc*4*i,heightInc*4, widthInc*4, heightInc*4), 10)
        if pos[1] < heightInc*12 and pos[1] > heightInc*8 and pos[0]> i*widthInc*4 and pos[0] < (i+1)*widthInc*4:
            draw.rect(screen, GREEN, (widthInc*4*i,heightInc*8, widthInc*4, heightInc*4), 10)
    for i in range (2):
        if widthInc*11 < pos[0] < widthInc*17 and heightInc*2 + heightInc*10*i < pos[1] < heightInc*4 + heightInc*10*i:
            draw.rect(screen, GREEN, (widthInc*11,heightInc*2 + heightInc*10*i, widthInc*6, heightInc*2), 10)
            
        if widthInc*19 < pos[0] < widthInc*21 and heightInc*2 + heightInc*10*i < pos[1] < heightInc*4 + heightInc*10*i:
            draw.rect(screen, GREEN, (widthInc*19,heightInc*2 + heightInc*10*i, widthInc*2, heightInc*2), 10)

    if selected != None:
        square0 = abs(1-square[0])
        draw.rect(screen, (0,255,255), (square[1], square0, square[2], square[3]), 10)



# A completely massive function which handles how selections work
def select(mouseObj, spots, current, state, hands):
    global filename
    if current  == None:
        mx, my = mouseObj.pos
        for i in range (0,2):
            for j in range(0,7):
                if widthInc*4*j < mx < widthInc*4*(j+1) and heightInc*4 + heightInc*4*(i) < my < heightInc*4 + heightInc*4*(i+1):
                    square = [i,j]
                    reversei = abs(1-i)
                    if spots[reversei][j].getOccupied():
                        if spots[reversei][j].getCard().getTired() == False:
                            filename = spots[reversei][j].getCard().getFilename()
                            return spots[reversei][j], [i*widthInc*4 + widthInc*4, j*heightInc*4, widthInc*4, heightInc*4], "B"
        for j in range(0,10):
            if tenth*j < mx < tenth*(j+1) and 0 < my < heightInc*2 :
                square = [i,j]
                print j, i
                if turn == 1:
                    filename = hands[0].getCards()[j].getFilename()
                    return [hands[0].getCards()[j], [0,j]], [0, j*tenth, tenth, heightInc*2], "H"

        for j in range(0,10): 
            if tenth*j < mx < tenth*(j+1) and heightInc*14 < my < heightInc*16 :
                square = [i,j]
                print j, i
                if turn == 0:
                    newfilename = hands[1].getCards()[j].getFilename()
                    filename = newfilename
                    print filename
                    return [hands[1].getCards()[j], [1,j]], [widthInc*14, j*tenth, tenth, heightInc*2], "H"
        murn = abs(1 - turn)
        if widthInc*11 < mx < widthInc*17 and heightInc*2 + heightInc*10*murn < my < heightInc*4 + heightInc*10*murn and board.getCurrentPlayer().getPower() > 0 and board.getCurrentPlayer().isReady():
            return 1, [widthInc*2 + widthInc*10*murn,heightInc*11, widthInc*6, heightInc*2], "C"
        elif widthInc*11 < mx < widthInc*17 and heightInc*2 + heightInc*10*murn < my < heightInc*4 + heightInc*10*murn and board.getCurrentPlayer().getPower() > 0:
            return  None, None, None
    else:
        mx, my = mouseObj.pos
        for i in range (0,2):
            for j in range(0,7):
                if widthInc*4*j < mx < widthInc*4*(j+1) and heightInc*4 + heightInc*4*(i) < my < heightInc*4 + heightInc*4*(i+1):
                    i = abs(1-i)
                    if state == "B":
                        if i != turn:
                            if spots[i][j].getOccupied():
                                fight(spots[i][j], current, board)
                                current = None
                                state = None
                            else:
                                NVT = NonValidTarget(screen)
                                NVT.displayMessage()
                                return None, None, None
                        else:
                            WT = WrongTurn(screen)
                            WT.displayMessage()
                            return None, None, None
                    #Play Card
                    elif state == "H":
                        if spots[i][j].getOccupied() == False:
                            board.playedCreature(current[0])
                            return playCard(board.getCurrentPlayer(), board.getCurrentPlayer().getCurMana(), current[0], spots[i][j],
											hands[current[1][0]], current[1][1])
                        else:
                            prevCard = spots[i][j].getCard()
                            canRight = checkRight([i,j], spots)
                            canLeft = checkLeft([i,j], spots)
                            if canLeft or canRight:
                                playCard(board.getCurrentPlayer(), board.getCurrentPlayer().getCurMana(), current[0], spots[i][j],
												hands[current[1][0]], current[1][1])

                                if mx > widthInc*4*j + widthInc*2 and canRight:
                                    shiftRight([i,j], spots, prevCard)
                                elif canLeft:
                                    shiftLeft([i,j], spots, prevCard)
                                elif canRight:
                                    shiftRight([i,j], spots, prevCard)
                                board.playedCreature(current[0])
                        return None, None, None
			#Hero attack
                    elif state == "C":
                        attacker = board.getCurrentPlayer()
                        if spots[i][j].getOccupied():
                            faceGo(attacker, spots[i][j], board)
                            attacker.setReady(False)
                            if attacker.isArmed():
                                weapon = attacker.getWeapon()
                                if weapon.attackCheck():
                                    attacker.unarmed()
                                    attacker.setWeapon(None)
                        return None, None, None
        if state == "B":
            if widthInc*11 < mx < heightInc*17 and heightInc*2 < my  <heightInc*4 and not (current.getCard().getTired()):
                goFace(current.getCard(), player1)
                return None, None, None
            elif widthInc*11 < mx < heightIinc*17 and  heightInc*12 < my  <heightInc*14 and not (current.getCard().getTired()):
                goFace(current.getCard(), player2)
                return None, None,  None
        elif state == "C":
            if widthInc*11 < mx < heightInc*17 and heightInc*2 < my  <heightInc*4 and player2.isReady():
                faceToFace(player1, player2)
                attacker = player2
                if attacker.isArmed():
                    weapon = attacker.getWeapon()
                    if weapon.attackCheck():
                        attacker.unarmed()
                        attacker.setWeapon(None)
            	return None, None, None
            elif widthInc*11 < mx < heightInc*17 and heightInc*12 < my  <heightInc*14 and player1.isReady():
            	faceToFace(player2, player1)
            	attacker = player1
            	if attacker.isArmed():
            		weapon = attacker.getWeapon()
            		if weapon.attackCheck():
            			attacker.unarmed()
            			attacker.setWeapon(None)
               	return None, None,  None
        
        return None, None, None

    return current, [i,j, widthInc*4, heightInc*5], state

#Play a card onto the board
def playCard(player, mana, card, spot, hand1, hand2):
    if card.getCost() <= player.getCurMana():
        player.changeCurMana(-card.getCost())
        spot.setCard(card)
        spot.setOccupied(True)
        hand1.setNull(hand2)
        
        if card.hasBattleCry():
            card.battleCry()
            
        if card.hasEffect():
            card.doEffect()
            board.playedCreature(card)
    display.flip()
    return None, None, None





#Initialize the board and Pygame
init()
size =(1600,800)
screen= display.set_mode(size)
width = screen.get_width()	
height = screen.get_height()

widthInc = width/32.0
heightInc = height/16.0

tenth = width/11.42

convx = width / 1600.0
convy = height/ 800.0

nameFont = font.Font(None, 30)
handFont = font.Font(None, 15)
selected = None
square = None
display.flip()
breaker = True
board = Board()
spots = board.getSpots()
hands = board.getHands()
player1 = board.getPlayer1()
player2 = board.getPlayer2()


twice = 0

state = None
x = 0
selecting = True
cardList = [CH_YETI(), FL_JUG(), RIV_CROC(), MUR_RAID(), ABU_SRG(board, screen), LNC_CAR(board, screen), IRN_OWL(board, screen), ELF_ARC(board, screen),
						GRM_MUR(board, screen), NOV_ENG(board, screen), LOT_HRD(board, screen)]
deck1Cards = []
deck2Cards = []
start = 0

choosing = True

#Initialize Player1's Deck
player1, deck1Cards, save1, name1 = selectScreen(player1, screen, board)

#Initialize Player2's Deck
player2, deck2Cards, save2, name2 = selectScreen(player2, screen, board)




selecting = True

if save1:
	Deck1 = open('deck1.txt', 'w')
	Deck1.write(name1+"\n")
	Deck1.write(player1.getRole()+"\n")
	for i in deck1Cards:
	    Deck1.write(i.getName()+"\n")
	Deck1.close()
	
if save2:        
	Deck2 = open('deck2.txt', 'w')
	Deck2.write(name2+"\n")
	Deck2.write(player2.getRole()+"\n")
	for i in deck2Cards:
	    Deck2.write(i.getName()+"\n")
	Deck2.close()


deck1, deck2 = board.simpleDecks(deck1Cards,deck2Cards, player1, player2)
hands[0].initialize(deck1)
hands[1].initialize(deck2)
lastpos = [1400, 0]
stat = 0
curpos = [1200, 0]

#GamePlay Loop
while (breaker):
		breaker = check_to_quit()
		#Draw the board
		drawGrid(screen, board, filename, lastpos, stat)
		#Highlight current mouse POS
		highlight(mouse.get_pos(), screen, selected, square)

		# Show minions on board
		showBoard(spots, screen)
        
		# Show cards in hand
		showHand(hands, screen, turn)
		time.wait(10)
		for newEvent in event.get():
				if newEvent.type == MOUSEBUTTONDOWN:
						selected, square, state = select(newEvent, spots, selected, state, hands)
						checkHeroPower(newEvent.pos, turn)
						turn = endTurn(newEvent.pos, turn, board, convx, convy)
						filename, stat = hoverCardMain(filename, newEvent.pos, spots, hands)
				elif newEvent.type == MOUSEMOTION:
						lastpos = newEvent.pos
						filename, stat = hoverCardMain(filename, newEvent.pos, spots, hands)
						curpos = newEvent.pos
				else:
						if newEvent.type == QUIT:
								breaker = False
		hoveredCard(screen, curpos, stat, filename)
		display.flip()
quit()
