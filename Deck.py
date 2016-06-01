from card import *
class Deck:
    def __init__(self, name, className):
        self.cardlist = []
        self.name = name
        self.className = className
        
    def draw(self):
        return self.cardlist.pop()
    
    def insertCard(self, card):
        if card.getClass() == self.className or card.getClass() == "neutral":
            self.cardlist.append(card)
            
    
        