# Card Template. Currently based on an obeslete template, will improve when
# spells, weapons and secrets are implemented.
class Card:
    def __init__(self, name, colour, cmc) :
        self.name = name;
        self.colour = colour;
        self.cmc = cmc;
    def __str__(self) :
        return self.name
    def getName(self):
        return self.name
    
#The Creature class represents a specific minion. 
# name: string of the card's full name
# power/toughness: the current and starting power and toughness of the card
# state: A marker to show if the card is on the board, hand or deck
# creatureType: Either None, or a string for the creaturetype
# owner: The player who owns it
# tired: True if it can attack, False otherwise
# buffs: List of the current buffs effecting the card
# effects: list of effects the card causes 
# screen: a reference to the screen
# img: a string of the filename for this card
# player: The player who selected ths card for his deck
# maxHealth: This maximum health this minion can heal too
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
        
        
    ######################
    #    Get Statements  #
    ######################
       
    def getMaxHealth (self):
        return self.maxHealth
    
    def getPlayer(self):
        return self.player
        
    def getFilename(self):
        return self.img
        
    def getCreatureType(self):
        return self.creatureType
        
    def getScreen(self):
        return self.screen
    
    def getOwner(self):
        return self.owner
    
    def getPower(self) :
        return self.power
    
    def getToughness(self) :
        return self.toughness

    def getTired(self):
        return self.tired
    
    def getName(self):
        return self.name
    
    def getCost(self):
        return self.cost
    
    def getBuffs(self):
        return self.buffs
    
    ######################
    #    Set Statements  #
    ######################
        
    def setScreen(self, screen):
        self.screen = screen
    
    def setTired(self, tire):
        self.tired = tire
        
    def setOwner(self, owner):
        self.owner = owner
  
    def setState(self, state):
        self.state = state
    
    def setPower(self, newT):
        self.power = newT
    
    def setToughness(self, newT):
        self.toughness = newT
        
    def setMaxHealth(self, maxh):
        self.maxHealth = maxh
        
    def setPlayer(self, player):
        self.player = player
    
   
    #By default these methods return False, but are overwritten on cards that 
    #have battlecries, effects or deathrattles
    def hasBattleCry(self):
        return False
    
    def hasDeathRattle(self):
        return False
    
    def hasEffect(self):
        return False
    
    def doEffect(self):
        pass
    
    def hasTaunt(self):
        return  False
    
    
    #A function that should be removed
    def ping(self, val=1):
        self.toughness = self.toughness - val
        
    #Add buff to the card
    def addBuff(self, buff):
        self.buffs.append(buff)
        
    #Remove all Buffs from the card    
    def clearBuffs(self):
        for buff in self.buffs:
            buff.removeBuff()
        self.buffs = []
        
    def removeBuff(self, buff):
        self.buffs.remove(buff)
        
   
    #Buff power by a set amount
    def incPower(self, inc):
        self.power = self.power + inc
        
    # Deals damage to the creature 
    def takeDamage(self, damage):
        self.toughness = self.toughness - damage
        

    #On Null creatures this function will be overwritten    
    def isNull(self):
        return False

    