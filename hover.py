from pygame import *
from card import *
from Spot import *
from Hand import *

#Return the filename of the last card hovered over in the card selection screen
def hoverCard(filename, pos, cards, start, convx, convy):
        for i in range (min(len(cards) - start, 4)):
            if 400*convx < pos[0] < 650*convx and convy*(80+50*i) < pos[1] < convy*(80+(50*(i+1))):
                    return foldername + cards[i + start].getFilename()
        return filename

#Return the filename of the last card hovered over in the main screen
def hoverCardMain(filename, pos, spots, hands):
    for i in range (0,10):
        if pos[1] < 100 and pos[0]> i*140 and pos[0] < (i+1)*140:
            return foldername + hands[0].getCards()[i].getFilename(), 1
        if pos[1] > 700 and pos[0]> i*140 and pos[0] < (i+1)*140:
            return foldername + hands[1].getCards()[i].getFilename(), 1
    for i in range (0,7):
        if pos[1] > 200 and pos[1] < 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
            if spots[1][i].getOccupied():
                return foldername + spots[1][i].getCard().getFilename(), 1
        if pos[1] < 700 and pos[1] > 400 and pos[0]> i*200 and pos[0] < (i+1)*200:
            if spots[0][i].getOccupied():
                return foldername + spots[0][i].getCard().getFilename(), 1
    return filename, 0