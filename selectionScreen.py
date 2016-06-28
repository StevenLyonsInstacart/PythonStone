from DrawBoard import *
from Generator import *
from hover import *
from inputbox import *


DISPLAYNUM = 4


def selectScreen(player, screen, board):
    deckCards = []
    selecting = True
    cardList = [CH_YETI(), FL_JUG(), RIV_CROC(), MUR_RAID(), ABU_SRG(board, screen), LNC_CAR(board, screen), IRN_OWL(board, screen), ELF_ARC(board, screen),
                        GRM_MUR(board, screen), NOV_ENG(board, screen), LOT_HRD(board, screen)]
    start = 0
    filename = "pics/Abusive_sergeant.png"
    saved = False
    name = ""
    while True:
        drawDeckChoice(screen)
        for evnt in event.get():
                    if evnt.type == MOUSEBUTTONDOWN:
                        outcome = makeOrBreak(evnt.pos)
                        if outcome[0]:
                            if outcome[0] == "Custom":
                                saved = outcome[1]
                                if saved:
                                    name = ask(screen, "Please Name Your Deck")
                                #Select screen for Player1
                                while (selecting):
                                        showSelect(screen, cardList, deckCards, 1, (255,255,255), start, filename, player.getPortrait())
                                        for evnt in event.get():
                                                if evnt.type == MOUSEBUTTONDOWN:
                                                        selecting = checkExit(evnt, player, deckCards)
                                                        newCard = addCard(evnt.pos, cardList, start, player)
                                                        updateClass(player, evnt.pos, board, screen)
                                                        if newCard:
                                                                if len(deckCards) < 30:
                                                                        deckCards.append(newCard)
                                                                else:
                                                                        ToManyCardsMessage = Message("Decks may only have 30 Cards", screen)
                                                                        ToManyCardsMessage.displayMessage()
                                                        start += updateList(evnt.pos)
                                                elif evnt.type == QUIT:
                                                        quit()
                                                elif evnt.type == MOUSEMOTION:
                                                        filename = hoverCard(filename, evnt.pos, cardList, start)
                                        display.flip()
                        
                            else:
                                deckData = []
                                readDeck = open('deck'+str(outcome[1] + 1)+'.txt', 'r')
                                for line in readDeck:
                                    deckData.append(line.strip('\n'))
                                readDeck.close()
                                
                                generator = Generator(screen, board, player)
                                cardDict = generator.getCardDict()
                                playerDict = generator.getPlayerDict()
                                
                                for i in deckData[2:]:
                                    deckCards.append(cardDict[i].copy())
                                playerData = playerDict[deckData[1]]
                                player.setPortrait(foldername + playerData[0])
                                player.setHP(playerData[1])
                                player.setRole(playerData[2])
                                
                        return player, deckCards, saved, name
                    elif evnt.type == QUIT:
                        quit()
        display.flip()
        

# Update the class that the player has picked on the deck selection screen.
def updateClass(player, pos, board, screen):
        classPort = [["guldan_portrait.jpg", WarlockPower(player), 'Warlock'], ["rexxar_portrait.jpg", HunterPower(player), 'Hunter'],
                                 ["garrosh_portrait.png", WarriorPower(player), 'Warrior'],["thrall_portrait.jpg", WarlockPower(player), 'Shaman']
                                 ,["uther_portrait.png", PaladinPower(player, board), 'Paladin'], ["jaina_portrait.jpg", MagePower(player, screen, board), 'Mage'],
                                 ["anduin_portrait.png", PriestPower(player, screen, board),'Priest'],["valeera_portrait.png", RoguePower(player),'Rogue'],
                                 ["malfurion_portrait.png", DruidPower(player), 'Druid']]
        for i in range (9):
            if 800 < pos[0] < 1050 and 80+30*i < pos[1] < 80+(30*(i+1)):
                    player.setPortrait(foldername + classPort[i][0])
                    player.setHP(classPort[i][1])
                    player.setRole(classPort[i][2])
                    
                    
#Check to see if User wants to quit the application
def check_to_quit():
        for evnt in event.get(): # checks all events that happen
                keys = key.get_pressed()
                keyz= key.get_pressed ()
                if evnt.type == QUIT:
                        return False
        return True

# Shift the DISPLAYNUM
def updateList(pos):
        if 400 < pos[0] < 500 and 400 < pos[1] < 500:
            return -DISPLAYNUM
        elif 600 < pos[0] < 700 and 400 < pos[1] < 500:
            return DISPLAYNUM
        return 0

#Check to see if User wants to submit Deck
def checkExit(mouse, player, deck):
        mx, my = mouse.pos
        if 1000 < mx < 1200 and 600 < my < 670:
                if not deck:
                        NoDeckMessage = Message("Please Select at least 1 Card", screen)
                        NoDeckMessage.displayMessage()
                        return True
                if player.getHP() == None:
                        NoDeckMessage = Message("Please Select a Character", screen)
                        NoDeckMessage.displayMessage()
                        return True
                return False
        else:
                return True
            
def makeOrBreak(pos):
    if 200 < pos[0] < 400 and 200 < pos[1] < 400:
        return ["Custom", False]
    elif  400 < pos[0] < 600 and 400 < pos[1] < 600:
        return ["Custom", True]
    for i in range (2):
        if 800 < pos[0] < 1050 and 80+30*i < pos[1] < 80+(30*(i+1)):
            return ["Past", i]
    return [False]

# Assign a card to a player
# returns a new card assigned to player (Card)
def addCard(pos, cards, start, player):
    for i in range (4):
        if 400 < pos[0] < 650 and 80+50*i < pos[1] < 80+(50*(i+1)):
            newCard = cards[i + start].copy()
            newCard.setPlayer(player)
            return newCard
    return None
