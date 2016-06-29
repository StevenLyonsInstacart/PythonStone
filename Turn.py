# This function is called at the end of each turn, to reset the board for the next player
# returns the Turn number (int)
def endTurn(pos, turn, board, convx, convy):
    
    # Getting the variables that need to be reset
    spots = board.getSpots()
    decks = board.getDecks()
    hands= board.getHands()
    player1 = board.getPlayer1()
    player2 = board.getPlayer2()
   
    
    if convx*1400<pos[0]<convx*1550 and convy*400 < pos[1] < convy*500:
    	board.getCurrentPlayer().setReady(False)
    	newPower = 0
        # Check if the player has a weapon
    	if board.getCurrentPlayer().isArmed():
    	    newPower += board.getCurrentPlayer().getWeapon().getPower()
        # Remove Buff to Players power
    	board.getCurrentPlayer().setPower(newPower)
        # Switch Current Player
    	board.getCurrentPlayer().getEnemy().setReady(True)
    	board.switchCurrent()
    	print "endTurn", turn
        
        # Give the new player updated mana and ste as ready
    	if turn == 1:
    	    player2.changeTotMana(1)
    	    player2.startTurn()
    	    player2.getHP().setTired(False)
    	    
    	else:
    	    player1.changeTotMana(1)
    	    player1.startTurn()
    	    player1.getHP().setTired(False)
    	 
        # Draw a card    
    	hands[turn].draw(decks[turn])
        # Set all current player minions to ready, and the enemies to tired
    	for j in range (7):
    	    if spots[turn][j].getOccupied():
        		spots[turn][j].getCard().setTired(True)
        		print "tired"
        # Update turn
    	turn = abs(1 - turn)
    	for j in range (7):
    	    if spots[turn][j].getOccupied():
        		spots[turn][j].getCard().setTired(False)
        		print "g2g"
        # Check all till end of turn buffs
    	checkBuffs(spots)
    	return turn
    else:
        return turn
# Finish all till end of turn buffs    
def checkBuffs(spots):
    for i in range (2):
        for j in range (7):
            if spots[i][j].getOccupied():
                buffs = spots[i][j].getCard().getBuffs()
                minion = spots[i][j].getCard()
                getRid = []
                for k in buffs:
                    if k.getOneTurn():
                        k.removeBuff()
                        getRid.append(k)
                for buf in getRid:
                    minion.removeBuff(buf)
	
