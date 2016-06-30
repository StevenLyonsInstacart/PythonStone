#Set the return to "blanks/" to begin with
# If you have images, use that foldername

turn = 0
board = None
screen = None

def setBoard(newBoard):
    global board 
    board = newBoard
    
def setScreen(newScreen):
    global screen 
    screen = newScreen
    
def getScreen():
    global screen
    return screen

def getBoard():
    global board
    return board

def getTurn():
    global turn
    return turn
def switchTurn():
    global turn
    turn = abs(1-turn)
def getFoldername():
    return "pics/"