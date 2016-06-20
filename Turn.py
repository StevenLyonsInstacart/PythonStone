def endTurn(pos, turn, board):
    spots = board.getSpots()
    decks = board.getDecks()
    hands= board.getHands()
    player1 = board.getPlayer1()
    player2 = board.getPlayer2()
   
    
    if 1400<pos[0]<1550 and 400 < pos[1] < 500:
	board.getCurrentPlayer().setReady(False)
	board.getCurrentPlayer().setPower(0)
	board.getCurrentPlayer().getEnemy().setReady(True)
	board.switchCurrent()
	print "endTurn", turn
	if turn == 1:
	    player2.changeTotMana(1)
	    player2.startTurn()
	    player2.getHP().setTired(False)
	    
	else:
	    player1.changeTotMana(1)
	    player1.startTurn()
	    player1.getHP().setTired(False)
	    
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
	
