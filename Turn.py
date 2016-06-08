def endTurn(pos, turn, board):
    spots = board.getSpots()
    decks = board.getDecks()
    hands= board.getHands()
    
    if 1400<pos[0]<1550 and 400 < pos[1] < 500:
	print "endTurn", turn
	if turn == 1:
	    board.changeTotMana2(1)
	    board.player2Turn()
	    
	else:
	    board.changeTotMana1(1)
	    board.player1Turn()
	    
	hands[turn].draw(decks[turn])
	for j in range (7):
	    if spots[turn][j].getOccupied():
		spots[turn][j].getCard().setTired(True)
		print "tired"
	turn = abs(1 - turn)
	for j in range (7):
	    if spots[turn][j].getOccupied():
		spots[turn][j].getCard().setTired(False)
		print "g2g"
	checkBuffs(spots)
	return turn
    else:
	return turn
    
def checkBuffs(spots):
    for i in range (2):
	for j in range (7):
	    if spots[i][j].getOccupied():
		buffs = spots[i][j].getCard().getBuffs()
		for k in buffs:
		    if k.getOneTurn():
			k.removeBuff()
	
