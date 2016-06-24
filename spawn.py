# Return True if there is a free spot to the right of the spot, False
# if there isn't
def checkRight(pos, spots):
    for i in range (pos[1], 7):
        if spots[pos[0]][i].getOccupied() == False:
            return True
    return False

# Return True if there is a free spot to the Left of the spot, False
# if there isn't
def checkLeft(pos, spots):
    if pos[1] == 6:
        return False
    for i in range (pos[1], 7):
        if spots[pos[0]][7 - i].getOccupied() == False:
            return True 
    return False

# Return True if there is a free spot on the given side of the board, False if not
# spots: One side of the board
def checkSpawn(spots):
    for i in range (7):
        if spots[6 - i].getOccupied() == False:
            return True
    return False

# Move Minions over to the left
def spawnLeft(spots, curCard):
    ind = 5
    while spots[ind].getOccupied():
    	holdover = spots[ind].getCard()
    	spots[ind].setCard(curCard)
    	curCard = holdover
    	ind -= 1
    holdover = spots[ind].getCard()
    spots[ind].setCard(curCard)
    spots[ind].setOccupied(True)
    curCard = holdover
    
#Move Minions over to the Right
def shiftLeft(pos, spots, curCard):
    ind = pos[1] + 1
    while spots[pos[0]][ind].getOccupied():
    	holdover = spots[pos[0]][ind].getCard()
    	spots[pos[0]][ind].setCard(curCard)
    	curCard = holdover
    	ind += 1
    holdover = spots[pos[0]][ind].getCard()
    spots[pos[0]][ind].setCard(curCard)
    spots[pos[0]][ind].setOccupied(True)
    curCard = holdover
    

def shiftRight(pos, spots, curCard):
    ind = pos[1] - 1
    while spots[pos[0]][ind].getOccupied():
	holdover = spots[pos[0]][ind].getCard()
	spots[pos[0]][ind].setCard(curCard)
	curCard = holdover
	ind -= 1
    holdover = spots[pos[0]][ind].getCard()
    spots[pos[0]][ind].setCard(curCard)
    spots[pos[0]][ind].setOccupied(True)
    curCard = holdover	
    
def spawnCreature(card, spots, board):
    canDo = checkSpawn(spots)
    curCard = None
    if canDo:
	if spots[6].getOccupied():
	    curCard = spots[6].getCard()
	spot = spots[6]
	spot.setCard(card)
	spot.setOccupied(True)
	if card.hasBattleCry():
	    card.battleCry()
			    
	if card.hasEffect():
	    card.doEffect()
	    board.playedCreature(card)
	if curCard:
	    return spawnLeft(spots, curCard)
    return False