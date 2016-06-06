from card import *
from random import *
from pygame import *
from Buffs import *
from Buff import *

RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BOARD = (205,182,139)
LINDSAY = (255, 7, 162)

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
	
def drawGrid(screen, board):
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
    
    player1Mana = nameFont.render(str(board.getCurMana1()) , True, (155,155,255 ), (0, 0, 0))
    manaRect = player1Mana.get_rect()
    manaRect.centerx = 1475 
    manaRect.centery = 150
    screen.blit(player1Mana, manaRect)
    
    player2Mana = nameFont.render(str(board.getCurMana2()) , True, (155,155,255 ), (0, 0, 0))
    mana2Rect = player2Mana.get_rect()
    mana2Rect.centerx = 1475 
    mana2Rect.centery = 650
    screen.blit(player2Mana, mana2Rect)
    
def showSelect(screen, cards, num, background):
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
    for i in range (7):
	name = nameFont.render(cards[num*i].getName() , True, (50,50,50), background)
	nameRect = name.get_rect()
	nameRect.centerx = 500 
	nameRect.centery = 100 + 50*i
	screen.blit(name, nameRect)
	