from card import *

# The deck class holds a custom selected 30 card deck
# cardlist: 30 cards in deck
# name: String for deck name
# classname: string of the class name, e.g. Warlock
class Deck:
    def __init__(self, name, className):
        self.cardlist = []
        self.name = name
        self.className = className
        
    def draw(self):
        return self.cardlist.pop()
    
    def insertCard(self, card):
        self.cardlist.append(card)
            
    
        