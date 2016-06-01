class Card:
    def __init__(self, name, colour, cmc) :
        self.name = name;
        self.colour = colour;
        self.cmc = cmc;
    def __str__(self) :
        return self.name
    def getName(self):
        return self.name
    

class Creature(Card):
    def __init__(self, name, cost, power, toughness) :
        self.name = name;
        self.power = power;
        self.cost = cost;
        self.toughness = toughness;
        self.state = None
    
    def hasBattleCry(self):
        return False
    
    def ping(self, val=1):
        self.toughness = self.toughness - val
        
    def getPower(self) :
        return self.power
    
    def setState(self, state):
        self.state = state
    
    def setPower(self, newT):
        self.power = newT
    
    def getToughness(self) :
        return self.toughness
    
    def setToughness(self, newT):
        self.toughness = newT
    
    def getName(self):
        return self.name
    
    def getCost(self):
        return self.cost

    