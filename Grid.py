from Hand import *
from Board import *
class Grid:
    def __init__(self):
        self.hand1 = Hand()
        self.hand2 = Hand()
        self.board = Board()
        
    def getBoard(self):
        return self.board