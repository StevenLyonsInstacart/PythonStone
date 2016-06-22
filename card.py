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
    def __init__(self, name, cost, power, toughness, owner) :
        self.name = name;
        self.power = power;
        self.cost = cost;
        self.toughness = toughness;
        self.state = None
        self.creatureType = None
        self.owner = owner
        self.tired = True
        self.buffs = []
        self.effects = []
        self.screen = screen
        self.img = ""
        self.player = None
        self.maxHealth = toughness
        
    def getMaxHealth (self):
        return self.maxHealth
    def setMaxHealth(self, maxh):
        self.maxHealth = maxh
        
    def setPlayer(self, player):
        self.player = player
        
    def isNull(self):
        return False
        
    def getPlayer(self):
        return self.player
        
    def getFilename(self):
        return self.img
        
    def getCreatureType(self):
        return self.creatureType
    
    def incPower(self, inc):
        self.power = self.power + inc
        
    def takeDamage(self, damage):
        self.toughness = self.toughness - damage
        
    def getScreen(self):
        return self.screen
    
    def setScreen(self, screen):
        self.screen = screen
        
    def getTired(self):
        return self.tired
    
    def setTired(self, tire):
        self.tired = tire
        
    def setOwner(self, owner):
        self.owner = owner
    
    def getOwner(self):
        return self.owner
        
    def hasBattleCry(self):
        return False
    
    def hasDeathRattle(self):
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
    
    def getBuffs(self):
        return self.buffs
    
    def addBuff(self, buff):
        self.buffs.append(buff)
        
    def clearBuffs(self):
        for buff in self.buffs:
            buff.removeBuff()
        self.buffs = []
        
    def hasEffect(self):
        return False
    
    def doEffect(self):
        pass

    