def endTurn(pos, turn, board):
    spots = board.getSpots()
    decks = board.getDecks()
    hands= board.getHands()
    
    if 1400<pos[0]<1550 and 400 < pos[1] < 500:
	print "endTurn"
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
	
	return turn
    else:
	return turn
	
