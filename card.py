from Constants import *
import MySQLdb
from networkx.algorithms.flow.mincost import cost_of_flow
from battlecries import *

# Card Template. Currently based on an obeslete template, will improve when
# spells, weapons and secrets are implemented.
class Card:
    def __init__(self, name, classType, cost, img) :
        self.name = name;
        self.classType = classType;
        self.cost = cost;
        self.img = img
        self.player = None
        
    def __str__(self) :
        return self.name
    
    def getName(self):
        return self.name
    
    def getClassType(self):
        return self.classType
    
    def getClass(self):
        return self.classType
    
    def getCost(self):
        return self.cost
    
    def getImg(self):
        return self.img
    def getFilename(self):
        return self.img
    
    def getPlayer(self):
        return self.player
    
    def setImg(self, img):
        self.img = img
    
    def setName(self, name):
        self.name = name
    
    def setClassType(self, classType):
        self.classType = classType
    
    def setCost(self, cost):
        self.cost = cost
        
    def setPlayer(self, playa):
        self.player = playa
        
    #On Null creatures this function will be overwritten    
    def isNull(self):
        return False
    
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
    def __init__(self, name, cost, power, toughness, owner, tired, buffs, effects, img, keywords, creaturetype, classType) :
        
        Card.__init__(self, name, classType, cost, img)
        self.power = power;
        self.toughness = toughness;
        self.state = None
        self.creatureType = creaturetype
        self.owner = owner
        self.tired = tired
        self.buffs = buffs
        self.effects = effects
        self.screen = getScreen()
        self.player = None
        self.keywords = keywords
        self.maxHealth = toughness
        self.ID = 0
        self.minion_id = -1
        self.classType = "neutral"
        self.battlecry = ''
        
        
    ######################
    #    Get Statements  #
    ######################
    
    def getMinionID (self):
        return self.minion_id
    
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
    
    def getBuffs(self):
        return self.buffs
    
    def getID(self):
        return self.ID
    
    def getKeywords(self):
        return self.keywords
    
    ######################
    #    Set Statements  #
    ######################
    
    def setMinionID (self, id):
        self.minion_id = id
        
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
        
    def setID(self, ID):
        self.ID = ID
        
    def setKeyword(self, key, ind):
        self.keywords[ind] = key
    
   
    #By default these methods return False, but are overwritten on cards that 
    #have battlecries, effects or deathrattles
    def hasBattleCry(self):
        print "RESULT EQUALS: "+self.battlecry != ''
        return self.battlecry != ''
    
    def hasDeathRattle(self):
        return False
    
    def hasEffect(self):
        return False
    
    def getType(self):
        return "Creature"
    
    def doEffect(self):
        pass
    
    def hasTaunt(self):
        return self.keywords[0]
    
    def battleCry(self):
        print "/n/nmmm/n/n"
        getBCs()[int(self.battlecry)]()
    
    
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
        if self.keywords[0]:
            board = getBoard()
            if self in board.getCurrentPlayer().getTaunts():
                board.getCurrentPlayer().removeTaunt(self)
            if self in board.getEnemyPlayer().getTaunts():
                board.getEnemyPlayer().removeTaunt(self)
        self.keywords = [False, False, False, False]
        
    def removeBuff(self, buff):
        self.buffs.remove(buff)
        
   
    #Buff power by a set amount
    def incPower(self, inc):
        self.power = self.power + inc
        
    # Deals damage to the creature 
    def takeDamage(self, damage):
        if self.keywords[2]:
            self.keywords[2] = False
        else:
            self.toughness = self.toughness - damage
            
    def copy(self):
        print self.name + " Break"
        return makeCreature(str(self.getMinionID()))

    def get_class_type(self):
        return self.__classType


    def set_class_type(self, value):
        self.__classType = value
        
    def setBattleCry(self, bat):
        self.battlecry = bat
        
class SQLcreature():
    def __init__(self, row) :
        self.id = row[0]
        self.name = row[1]
        self.attack = row[2]
        self.health = row[3]
        self.cost = row[4]
        self.class_type = row[5]
        self.battlecry = row[6]
        self.deathrattle = row[7]
        self.effect = row[8]
        self.img = row[10].strip("\"")
        self.keywords = [bool(row[11]), bool(row[12]), bool(row[13]), bool(row[14])]
        self.battleCry = row[15]
        self.reference = row
        
    def getID (self):
        return self.id

    def get_reference(self):
        return self.reference

    def get_name(self):
        return self.name


    def get_attack(self):
        return self.attack


    def get_health(self):
        return self.health


    def get_cost(self):
        return self.cost


    def get_class_type(self):
        return self.class_type


    def get_battlecry(self):
        return self.battlecry


    def get_deathrattle(self):
        return self.deathrattle


    def get_effect(self):
        return self.effect


    def get_img(self):
        return self.img
    
    def getKeywords(self):
        return self.keyword
    
    def setKeywords(self, keyword):
        self.keywords = keyword
    
    def setID (self, id):
        self.id = id


    def set_name(self, value):
        self.name = value


    def set_attack(self, value):
        self.attack = value


    def set_health(self, value):
        self.health = value


    def set_cost(self, value):
        self.cost = value


    def set_class_type(self, value):
        self.class_type = value


    def set_battlecry(self, value):
        self.battlecry = value


    def set_deathrattle(self, value):
        self.deathrattle = value


    def set_effect(self, value):
        self.effect = value


    def set_img(self, value):
        self.img = value
    
    def generate_creature(self):
        tired = not self.keywords[1]
        newCreature = Creature(self.name, self.cost, self.attack, self.health, 0, tired, 
     [], None, self.img, self.keywords , None, self.class_type)
        newCreature.setMinionID(self.getID())
        newCreature.setBattleCry('1')
        return newCreature



def makeCreature(minion_id):
    db = MySQLdb.connect("localhost","root","root","sys" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    print "SELECT * FROM sys.minion WHERE minion_id = "+str(minion_id)
    cursor.execute("SELECT * FROM sys.minion WHERE minion_id = "+str(minion_id))
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print data
    newCreature = SQLcreature(data)
    # disconnect from server
    db.close()
    print "Success"
    return newCreature.generate_creature()




class Spell(Card):
    def __init__(self, name, classType, cost, img):
        Card.__init__(self, name, classType, cost, img)
        
    def chooseOne(self):
        pass
    
    def overload(self):
        pass
    
    def doSpell(self, pos):
        pass
    
    def getType(self):
        return "Spell"
    
makeCreature("1")