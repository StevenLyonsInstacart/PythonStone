from card import *
class Hand:
    def __init__(self):
        self.name = 3
        self.cards = []
        for i in range (10):
            self.cards.append(Creature("Yeti", 4, 4, 5))
            
    def getCards(self):
        return self.cards