from pygame import *
from random import *

from Buff import *
from Buffs import *
from card import *
from Constants import *


foldername = foldername()
DISPLAYNUM = 4

RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BOARD = (205,182,139)
LINDSAY = (255, 7, 162)


#Show all of the Cards on the Board
def showBoard(spots, screen):
    for i in range(0,2):
        for j in range(7):
            if (spots[i][j].getOccupied()):
                if i != 0:
                    showCard2(spots[i][j], screen, True)
                else:
                    showCard2(spots[i][j], screen, False)
                    
                    
# Show all of the cards in Hand of the current Player
# hands: each player's hand
# screen: the surface being projected onto
# turn: an int representation of who's turn it is		
def showHand(hands, screen, turn):
    
    #The opposing Player's cards will be shown as cardbacks
    cardBack = image.load(foldername+"cardback.png")
    for i in range (2):
        for j in range (10):
            if i != turn:
                showHandCard(hands[i].getCards()[j], [i,j], screen)
            else:
                showCardBack(hands[i].getCards()[j], [j,i], screen, cardBack)

#Shows a cardBack		
def showCardBack(card, pos, screen, img):
    if card.isNull() == False:
	imgRect = Rect(pos[0]*140, 700*pos[1], 140, 100)
	screen.blit(img, imgRect)
    
	
# Show a card on the Board
# row1: A bool used to see what player the card belongs too       
def showCard2(spot, screen, row1):
    #Name Text
    nameFont = font.Font(None, 30)
    name = nameFont.render(spot.getCard().getName() , True, (255, 255, 255), BOARD)
    nameRect = name.get_rect()
    nameRect.centerx = spot.getPos()[0] +25
    if row1:
        nameRect.centery = spot.getPos()[1] + 50
    else:
        nameRect.centery = spot.getPos()[1]
        
    #Power Toughness Text
    pts = str(spot.getCard().getPower()) + "                  " + str(spot.getCard().getToughness())
    pt = nameFont.render(pts, True, (255, 255, 255), BOARD)
    ptRect = pt.get_rect()
    ptRect.centerx = spot.getPos()[0] + 30
    if row1:
        ptRect.centery = spot.getPos()[1] + 150
    else:
        ptRect.centery = spot.getPos()[1] + 100
        
    #Blit to Screen
    screen.blit(name, nameRect)
    screen.blit(pt, ptRect)

#Shows a hand card    
def showHandCard(card, pos, screen):
    handFont = font.Font(None, 15)
    if card.getName() != "Null":
        #Name Text
    	name = handFont.render(card.getName() , True, (255, 255, 255), BOARD)
    	nameRect = name.get_rect()
    	nameRect.centerx = pos[1]*140 + 70
    	nameRect.centery = pos[0]*700 + 20
    	
        #Cost Text
    	cost = handFont.render(str(card.getCost()) , True, (255, 255, 255), BOARD)
    	costRect = cost.get_rect()
    	costRect.centerx = pos[1]*140 + 70
    	costRect.centery = pos[0]*700 + 40
    	
        #Blit to Screen
    	screen.blit(name, nameRect)
    	screen.blit(cost, costRect)

#The main draw method, used to continuosly draw the board
# filename is the name of the current hovercard
# pos is the mouse position
# status is an int used to determine if the hovercard should be shown	
def drawGrid(screen, board, filename, pos=[0,0], status=0):
    
    #establish the players
    player1 = board.getPlayer1()
    player2 = board.getPlayer2()
    
    nameFont = font.Font(None, 30)
    #Base coat of the board
    draw.rect(screen, BOARD, (0,0,1400,800))
    
    #Player1 Portrait
    player1 = board.getPlayer1()
    portrait1 = image.load(player1.getPortrait())
    port1Rect = Rect(550, 100, 300, 100)
    screen.blit(portrait1, port1Rect)
    
    #Player2 Portrait
    player2 = board.getPlayer2()
    portrait2 = image.load(player2.getPortrait())
    port2Rect = Rect(550, 600, 300, 100)
    screen.blit(portrait2, port2Rect)
    
    #Player1 Armor
    crest = image.load("pics/armor.png")
    crest1Rect = Rect(900, 150, 40, 45)
    screen.blit(crest, crest1Rect)
    
    #Player2 Armor
    crest = image.load("pics/armor.png")
    crest2Rect = Rect(900, 650, 40, 45)
    screen.blit(crest, crest2Rect)
    
    #Player1 Health
    health1 = nameFont.render((str(player1.getLife()) +"    "+ str(player1.getArmor())) , True, (255, 255, 255), BOARD)
    health1Rect = health1.get_rect()
    health1Rect.centerx = 900
    health1Rect.centery = 120
    screen.blit(health1, health1Rect)
    
    #Player1 Weapon
    if player1.isArmed():
    	weapon = player1.getWeapon()
        
    	Weapon1 = nameFont.render((str(weapon.getPower()) +" / "+ str(weapon.getDurability())) , True, (255, 255, 255), BOARD)
    	Weapon1Rect = Weapon1.get_rect()
    	Weapon1Rect.centerx = 300
    	Weapon1Rect.centery = 150
    	screen.blit(Weapon1, Weapon1Rect)
	
    #Player2 Weapon
    if player2.isArmed():
    	weapon = player2.getWeapon()
        
    	Weapon2 = nameFont.render((str(weapon.getPower()) +" / "+ str(weapon.getDurability())) , True, (255, 255, 255), BOARD)
    	Weapon2Rect = Weapon2.get_rect()
    	Weapon2Rect.centerx = 300
    	Weapon2Rect.centery = 650
    	screen.blit(Weapon2, Weapon2Rect)
	
	#Player 2 Health
    health2 = nameFont.render((str(player2.getLife()) +"    "+ str(player2.getArmor())) , True, (255, 255, 255), BOARD)
    health2Rect = health1.get_rect()
    health2Rect.centerx = 900
    health2Rect.centery = 620
    screen.blit(health2, health2Rect)
    
    
    #Verticals
    for i in range (1,7):
	draw.line(screen, RED, (200*i, 200) , (200*i, 600))
        
    for i in range (1,10):
	draw.line(screen, RED, (140*i, 0) , (140*i, 100))
	draw.line(screen, RED, (140*i, 700) , (140*i, 800))
	
    #Horizontals
    draw.line(screen, RED, (0, 100) , (1400, 100))
    draw.line(screen, RED, (0, 200) , (1400, 200))
    draw.line(screen, RED, (0, 600) , (1400, 600))
    draw.line(screen, RED, (0, 700) , (1400, 700))
    
    
    #Hero Section 1
    draw.line(screen, RED, (450, 100), (450, 200))
    draw.line(screen, RED, (450, 600), (450, 700))
    draw.line(screen, RED, (550, 100), (550, 200))
    draw.line(screen, RED, (550, 600), (550, 700))
    
    #Hero Section 2
    draw.line(screen, RED, (850, 100), (850, 200))
    draw.line(screen, RED, (850, 600), (850, 700))
    draw.line(screen, RED, (950, 100), (950, 200))
    draw.line(screen, RED, (950, 600), (950, 700))
    
    #Hero Power Boxes
    draw.rect(screen, BLUE, (950, 100, 100, 100))
    draw.rect(screen, BLUE, (950, 600, 100, 100))
    
    
    #End Turn Button
    draw.rect(screen, (100, 100, 255), (1400,400,150,100))
    name = nameFont.render("End Turn" , True, (155,155,255 ), (100, 100, 0))
    nameRect = name.get_rect()
    nameRect.centerx = 1475 
    nameRect.centery = 450
    screen.blit(name, nameRect)
    
    #Player 1 Mana
    player1Mana = nameFont.render(str(player1.getCurMana()) , True, (155,155,255 ), (0, 0, 0))
    manaRect = player1Mana.get_rect()
    manaRect.centerx = 1475 
    manaRect.centery = 150
    screen.blit(player1Mana, manaRect)
    
    #Player 1 Power
    player1Power = nameFont.render(str(player1.getPower()) , True, (205,155,20), BOARD)
    powerRect = player1Power.get_rect()
    powerRect.centerx = 500
    powerRect.centery = 150
    screen.blit(player1Power, powerRect)
    
    #Player 2 Power
    player2Power = nameFont.render(str(player2.getPower()) , True, (205,155,20), BOARD)
    power2Rect = player2Power.get_rect()
    power2Rect.centerx = 500
    power2Rect.centery = 650
    screen.blit(player2Power, power2Rect)
    
    #Player 2 Mana
    player2Mana = nameFont.render(str(player2.getCurMana()) , True, (155,155,255 ), (0, 0, 0))
    mana2Rect = player2Mana.get_rect()
    mana2Rect.centerx = 1475 
    mana2Rect.centery = 650
    screen.blit(player2Mana, mana2Rect)
    

#Shows a card image if mouse is hovering over the card    
def hoveredCard(screen, pos, status, filename):
        if status == 1:
            img = image.load(filename)
            #Check where the card should go to not be off screen
            if pos[1] > 184:
                imgRect = Rect(pos[0], pos[1] - 184, 184, 254)
            else:
                imgRect = Rect(pos[0], pos[1], 184, 254)
            screen.blit(img, imgRect)
            display.flip()
            
    
def showSelect(screen, cards, num, background, start, filename):
    nameFont = font.Font(None, 30)
    draw.rect(screen, background, (0,0,1400,800))
    
    
    
    #Finish  Deck Building
    draw.rect(screen, RED, (1000,600, 200, 70), 5)
    
    name = nameFont.render("Submit Deck" , True, (50,50,50), background)
    nameRect = name.get_rect()
    nameRect.centerx = 1100 
    nameRect.centery = 635
    screen.blit(name, nameRect)
    
    
    
    draw.rect(screen, GREEN, (400, 80, 250, 170), 10 )
    for i in range (start, min(start + DISPLAYNUM, len(cards))):
	name = nameFont.render(cards[num*i].getName() , True, (50,50,50), background)
	nameRect = name.get_rect()
	nameRect.centerx = 500 
	nameRect.centery = 100 + 50*(i - start)
	screen.blit(name, nameRect)
	
    draw.rect(screen, BLUE, (800, 80, 250, 270), 10)
    classes = ["Warlock","Hunter","Warrior","Shaman","Paladin","Mage","Priest","Rogue","Druid"]
    for i in range (9):
	name = nameFont.render(classes[i], True, (50,50,50), background)
	nameRect = name.get_rect()
	nameRect.centerx = 925 
	nameRect.centery = 95 + 30*i
	screen.blit(name, nameRect)
	
    for i in range (9):
	draw.line(screen, BLUE, (800, 80 + 30*i), (1050, 80 + 30*i))
    
    draw.rect(screen, BLUE, (400, 400, 100, 100))
    draw.rect(screen, RED, (600, 400, 100, 100))
    
    img = image.load(filename)
    imgRect = Rect(1400, 0, 200, 200)
    screen.blit(img, imgRect)