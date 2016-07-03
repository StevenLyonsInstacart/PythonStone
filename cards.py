from pygame import *
from random import *

from StringIO import *

import requests
import urllib
import os.path




from Buff import *
from Buffs import *
from Damage import *
from DrawBoard import *
from Effect import *
from Effects import *
from card import *
from Constants import *
import unirest

#Colours
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BOARD = (205,182,139)

VANILLA =  [False, False, False, False]
TAUNT =    [True, False, False, False ]
CHARGE =   [False, True, False, False ]
DIVINE =   [False, False, True, False ]
WINDFURY = [False, False, False, True ]


def getImage(cardName, saveName): 
    response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/"+cardName,
                           headers={"X-Mashape-Key": "QrzUPBv9wAmshvo7g3fypeqSwQPCp1KZuo7jsnuMK9B8m1ZTkY",
                                    "Accept": "application/json"
                                    }
                           )
    print response.body[0]['img']
    urllib.urlretrieve(response.body[0]['img'], saveName)


   


#Null Creature is an empty creature that wont be shown on screen.
#Currently Null_Creature is used in empty board and hand spaces
class NULL_CREATURE(Creature):
    def __init__(self):
        self.name = "Null"
        self.power = 0
        self.toughness = 0
	self.maxHealth = 0
        self.cost = 0
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
	self.buffs = []
	self.img = "abusive_sergeant.png"
    
    
#Representation of Chillwind Yeti    
class CH_YETI(Creature):
    def __init__(self):
        self.name = "Chillwind Yeti"
        self.power = 4
        self.toughness = 5
	self.maxHealth = 5
        self.cost = 4
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"chillwind_yeti.png"):
            pass
        else:
            getImage("Chillwind%20Yeti", foldername+"chillwind_yeti.png")
        self.img = "chillwind_yeti.png"
	
    def getClass(self):
        return self.classType
    
    def copy(self):
        return CH_YETI()
    
#Representation of River Crocolisk    
class RIV_CROC(Creature):
    def __init__(self):
        self.name = "River Crocolisk"
        self.power = 2
        self.toughness = 3
	self.maxHealth = 3
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = "Beast"
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"river_crocolisk.png"):
            pass
        else:
            getImage("River%20Crocolisk", foldername+"river_crocolisk.png")      
        self.img = "river_crocolisk.png"
	
        
    def getClass(self):
        return self.classType
    def copy(self):
        return RIV_CROC()
    
#The Taunts
    
# Representation of Goldshire Footman    
class GLD_FOT(Creature):
    def __init__(self):
        self.name = "Goldshire Footman"
        self.power = 1
        self.toughness = 2
        self.maxHealth = 2
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = TAUNT
        if os.path.isfile(foldername+"goldshire_footman.png"):
            pass
        else:
            getImage("Goldshire%20Footman", foldername+"goldshire_footman.png")      
        self.img = "goldshire_footman.png"
    
    def hasTaunt(self):
        return True
        
    def getClass(self):
        return self.classType
    def copy(self):
        return GLD_FOT()
    
 #Representation of Frostwolf Grunt   
class FRT_GRT(Creature):
    def __init__(self):
        self.name = "Frostwolf Grunt"
        self.power = 2
        self.toughness = 2
        self.maxHealth = 2
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = TAUNT
        if os.path.isfile(foldername+"frostwolf_grunt.png"):
            pass
        else:
            getImage("frostwolf%20grunt", foldername+"frostwolf_grunt.png")      
        self.img = "frostwolf_grunt.png"
    
    def hasTaunt(self):
        return True
        
    def getClass(self):
        return self.classType
    def copy(self):
        return FRT_GRT()
    
#Representation of Ironfur Grizzly   
class IRN_GRZ(Creature):
    def __init__(self):
        self.name = "Ironfur Grizzly"
        self.power = 3
        self.toughness = 3
        self.maxHealth = 3
        self.cost = 3
        self.classType = "neutral"
        self.creatureType = "Beast"
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = TAUNT
        if os.path.isfile(foldername+"ironfur_grizzly.png"):
            pass
        else:
            getImage("ironfur%20grizzly", foldername+"ironfur_grizzly.png")      
        self.img = "ironfur_grizzly.png"
    
    def hasTaunt(self):
        return True
        
    def getClass(self):
        return self.classType
    def copy(self):
        return IRN_GRZ()
    
#Representation of Silverback Patriarch   
class SLV_PAT(Creature):
    def __init__(self):
        self.name = "Silverback Patriarch"
        self.power = 1
        self.toughness = 4
        self.maxHealth = 4
        self.cost = 3
        self.classType = "neutral"
        self.creatureType = "Beast"
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = TAUNT
        if os.path.isfile(foldername+"silverback_patriarch.png"):
            pass
        else:
            getImage("silverback%20patriarch", foldername+"silverback_patriarch.png")      
        self.img = "silverback_patriarch.png"
    
    def hasTaunt(self):
        return True
        
    def getClass(self):
        return self.classType
    def copy(self):
        return SLV_PAT()
    
#Representation of Lord of the Arena  
class LRD_ARN(Creature):
    def __init__(self):
        self.name = "Lord of the Arena"
        self.power = 6
        self.toughness = 5
        self.maxHealth = 5
        self.cost = 6
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = TAUNT
        if os.path.isfile(foldername+"lord_of_the_arena.png"):
            pass
        else:
            getImage("lord%20of%20the%20arena", foldername+"lord_of_the_arena.png")      
        self.img = "lord_of_the_arena.png"
    
    def hasTaunt(self):
        return True
        
    def getClass(self):
        return self.classType
    def copy(self):
        return LRD_ARN()
    
#Representation of Booty Bay Bodyguard  
class BOT_BAY(Creature):
    def __init__(self):
        self.name = "Booty Bay Bodyguard"
        self.power = 5
        self.toughness = 4
        self.maxHealth = 4
        self.cost = 5
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = TAUNT
        if os.path.isfile(foldername+"booty_bay_bodyguard.png"):
            pass
        else:
            getImage("booty%20bay%20bodyguard", foldername+"booty_bay_bodyguard.png")      
        self.img = "booty_bay_bodyguard.png"
    
    def hasTaunt(self):
        return True
        
    def getClass(self):
        return self.classType
    def copy(self):
        return BOT_BAY()
    
#Representation of Booty Bay Bodyguard  
class SEN_JIN(Creature):
    def __init__(self):
        self.name = "Sen'jin Shieldmasta"
        self.power = 3
        self.toughness = 5
        self.maxHealth = 5
        self.cost = 4
        self.classType = "neutral"
        self.creatureType = None
        self.battleCry = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = TAUNT
        if os.path.isfile(foldername+"senjin_shieldmasta.png"):
            pass
        else:
            getImage("sen%27jin%20shieldmasta", foldername+"senjin_shieldmasta.png")      
        self.img = "senjin_shieldmasta.png"
    
    def hasTaunt(self):
        return True
        
    def getClass(self):
        return self.classType
    def copy(self):
        return SEN_JIN()
    
#############################
####    Charge Minions    ###
#############################

#Representation of Stonetusk Boar

class STN_BOR(Creature):
    def __init__(self):
        
        if os.path.isfile(foldername+"stonetusk_boar.png"):
            pass
        else:
            getImage("stonetusk%20boar", foldername+"stonetusk_boar.png")      
        Creature.__init__(self, "Stonetusk Boar", 1, 1, 1, 0, False, [], [], "stonetusk_boar.png", CHARGE, None, "neutral")
        
    def getClass(self):
        return self.classType
    def copy(self):
        return STN_BOR()
    
# Bluegill Warrior representation    
class BLU_WAR(Creature):
    def __init__(self):
        if os.path.isfile(foldername+"bluegill_warrior.png"):
            pass
        else:
            getImage("bluegill%20warrior", foldername+"bluegill_warrior.png")      
        Creature.__init__(self, "Bluegill Warrior", 2, 2, 1, 0, False, [], [], "bluegill_warrior.png", CHARGE, "Murloc", "neutral")
        
    def getClass(self):
        return self.classType
    def copy(self):
        return BLU_WAR()

# Wolfrider representation    
class WLF_RID(Creature):
    def __init__(self):
        if os.path.isfile(foldername+"Wolfrider.png"):
            pass
        else:
            getImage("wolfrider", foldername+"wolfrider.png")      
        Creature.__init__(self, "Wolfrider", 3, 3, 1, 0, False, [], [], "wolfrider.png", CHARGE, None, "neutral")
        
    def getClass(self):
        return self.classType
    def copy(self):
        return WLF_RID()
    
    
# Wolfrider representation    
class STR_KNT(Creature):
    def __init__(self):
        if os.path.isfile(foldername+"stormwind_knight.png"):
            pass
        else:
            getImage("stormwind%20knight", foldername+"stormwind_knight.png") 
        Creature.__init__(self, "Stormwind Knight", 4, 2, 5, 0, False, [], [], "stormwind_knight.png", CHARGE, None, "neutral")
        
    def getClass(self):
        return self.classType
    def copy(self):
        return STR_KNT()

# Reckless Rocketeer representation    
class REK_ROC(Creature):
    def __init__(self):
        if os.path.isfile(foldername+"reckless_rocketeer.png"):
            pass
        else:
            getImage("reckless%20rocketeer", foldername+"reckless_rocketeer.png") 
        Creature.__init__(self, "Reckless Rocketeer", 6, 5, 2, 0, False, [], [], "reckless_rocketeer.png", CHARGE, None, "neutral")
        
    def getClass(self):
        return self.classType
    def copy(self):
        return REK_ROC()
    
    
##########################
##    Divine Minions    ##
##########################

# Argent Squire representation    
class ARG_SQU(Creature):
    def __init__(self):
        if os.path.isfile(foldername+"argent_squire.png"):
            pass
        else:
            getImage("argent%20squire", foldername+"argent_squire.png") 
        Creature.__init__(self, "Argent Squire", 1, 1, 1, 0, True, [], [], "argent_squire.png", DIVINE, None, "neutral")
        
    def getClass(self):
        return self.classType
    def copy(self):
        return ARG_SQU()
    
class SCR_CRU(Creature):
    def __init__(self):
        if os.path.isfile(foldername+"scarlet_crusader.png"):
            pass
        else:
            getImage("scarlet%20crusader", foldername+"scarlet_crusader.png") 
        Creature.__init__(self, "Scarlet Crusader", 3, 3, 1, 0, True, [], [], "scarlet_crusader.png", DIVINE, None, "neutral")
        
    def getClass(self):
        return self.classType
    def copy(self):
        return SCR_CRU()
    
class ARG_COM(Creature):
    def __init__(self):
        if os.path.isfile(foldername+"argent_commander.png"):
            pass
        else:
            getImage("argent%20commander", foldername+"argent_commander.png") 
        Creature.__init__(self, "Argent Commander", 6, 4, 2, 0, False, [], [], "argent_commander.png", [False, True, True, False], None, "neutral")
        
    def getClass(self):
        return self.classType
    def copy(self):
        return ARG_COM()
    
# Argent Squire representation    
class AL_AKIR(Creature):
    def __init__(self):
        if os.path.isfile(foldername+"alakir_the_windlord.png"):
            pass
        else:
            getImage("al%27akir%20the%20windlord", foldername+"alakir_the_windlord.png") 
        Creature.__init__(self, "Al'akir the Windlord", 8, 3, 5, 0, False, [], [], "alakir_the_windlord.png", [True, True, True, True], None, "neutral")

        
    def getClass(self):
        return self.classType
    def copy(self):
        return AL_AKIR()    
    
    def hasTaunt(self):
        return True



    
#Representation of Flame Juggler    
class FL_JUG(Creature):
    
    #BattleCry: deal 1 damage to a random enemy
    def battleCry(self):
        curBoard = self.state.getBoard()
        enemySide = curBoard.getSpots()[1]
        sanity = 0
        check = int(random()*7)
        while (enemySide[check].getOccupied() == False and sanity<100):
            sanity += 1
            check = int(random()*7)
        if sanity < 100:
            card = enemySide[check].getCard()
            card.ping()           
        
    def __init__(self):
        self.name = "Flame Juggler"
        self.power = 2
        self.toughness = 3
	self.maxHealth = 3
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"flame_juggler.png"):
            pass
        else:
            getImage("Flame%20Juggler", foldername+"flame_juggler.png") 
        self.img = "flame_juggler.png"
	
    def getClass(self):
        return self.classType
    
    def copy(self):
        return FL_JUG()
    #Has a battlecry    
    def hasBattleCry(self):
        return True

#Representation of Murloc Raider    
class MUR_RAID(Creature):
    
    def __init__(self):
        self.name = "Murloc Raider"
        self.power = 2
        self.toughness = 1
	self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = "Murloc"
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"murloc_raider.png"):
            pass
        else:
            getImage("Murloc%20Raider", foldername+"murloc_raider.png") 
        self.img = "murloc_raider.png"
        
    def copy(self):
        return MUR_RAID()
    
    def getClass(self):
        return self.classType
    
#Representation of Grimscale Oracle    
class GRM_MUR(Creature):
    
    def __init__(self):
        self.name = "Grimscale Oracle"
        self.power = 1
        self.toughness = 1
        self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = "Murloc"
        self.owner = 0
        self.tired = True
        self.board = getBoard()  
        self.screen = getScreen()
        self.buffs = []
        self.keywords = VANILLA
        self.effects = [GRM_EFF(board, self)]
        if os.path.isfile(foldername+"grimscale_oracle.png"):
            pass
        else:
            getImage("grimscale%20oracle", foldername+"grimscale_oracle.png") 
        self.img = "grimscale_oracle.png"
        self.ID = -1
        
    def copy(self):
        return GRM_MUR()
    
    def getClass(self):
        return self.classType
    
    def hasEffect(self):
        return True
    
    #Buff all other murlocs with +1 attack
    def doEffect(self):
        self.board.addEffect(self.effects[0])
        self.effects[0].onPlay()
    
#Representation of Abusive Sergeant    
class ABU_SRG(Creature):
    
    def __init__(self):
        self.name = "Abusive Sergeant"
        self.power = 2
        self.toughness = 1
        self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = getBoard()  
        self.screen = getScreen()
        self.buffs = []
        self.keywords = VANILLA
        self.effects = []
        if os.path.isfile(foldername+"abusive_sergeant.png"):
            pass
        else:
            getImage("Abusive%20Sergeant", foldername+"abusive_sergeant.png")
        self.img = "abusive_sergeant.png"
        
    def copy(self):
        return ABU_SRG()
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    #Give a minion +2 attack until end of turn
    def battleCry(self):
        selectedBattleCry(ABU_BUFF(None), self.img)

#Lance Carrier Representation	
class LNC_CAR(Creature):
    
    def __init__(self):
        self.name = "Lance Carrier"
        self.power = 1
        self.toughness = 2
        self.maxHealth = 2
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = getBoard()  
        self.screen = getScreen()
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"lance_carrier.png"):
            pass
        else:
            getImage("Lance%20Carrier", foldername+"lance_carrier.png") 
        self.img = "lance_carrier.png"
        
    def copy(self):
        return LNC_CAR()
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    #Ggive a minion +2 attack permanently
    def battleCry(self):
        selectedBattleCry(LNC_BUFF(None), self.img)
	
#Representation of IronBeak Owl    
class IRN_OWL(Creature):
    
    def __init__(self):
        self.name = "Iron Beak Owl"
        self.power = 2
        self.toughness = 1
        self.maxHealth = 1
        self.cost = 3
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = getBoard()  
        self.screen = getScreen()
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"ironbeak_owl.png"):
            pass
        else:
            getImage("Ironbeak%20Owl", foldername+"ironbeak_owl.png") 
        self.img = "ironbeak_owl.png"
        
    def copy(self):
        return IRN_OWL()
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    #Silence a Creature
    def battleCry(self):
        selectedBattleCry(OWL_BUFF(None), self.img)

#Representation of Novice Engineer	
class NOV_ENG(Creature):
    
    def __init__(self):
        self.name = "Novice Engineer"
        self.power = 1
        self.toughness = 1
        self.maxHealth = 1
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = getBoard()  
        self.screen = getScreen()
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"novice_engineer.png"):
            pass
        else:
            getImage("Novice%20Engineer", foldername+"novice_engineer.png") 
        self.img = "novice_engineer.png"
        
    def copy(self):
        return NOV_ENG()
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    #Draw a card
    def battleCry(self):
        player = self.getPlayer()
        player.getHand().draw(player.getDeck())

#Representation of Silver Hand Recruit	
class DUDE(Creature):
    
    def __init__(self):
        self.name = "SilverHand recruit"
        self.power = 1
        self.toughness = 1
        self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.buffs = []
        self.keywords = VANILLA
        self.img = "silverhand_recruit.png"
        
    def copy(self):
        return DUDE()
    
    def getClass(self):
        return self.classType
    
#Rrepresentation of Loot Hoarder	
class LOT_HRD(Creature):
    
    def __init__(self):
        self.name = "Loot Hoarder"
        self.power = 2
        self.toughness = 1
        self.maxHealth = 1
        self.cost = 2
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = getBoard()  
        self.screen = getScreen()
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"loot_hoarder.png"):
            pass
        else:
            getImage("Loot%20Hoarder", foldername+"loot_hoarder.png") 
        self.img = "loot_hoarder.png"
        
    def copy(self):
        return LOT_HRD()
    
    def getClass(self):
        return self.classType
    
    def hasDeathRattle(self):
        return True
    
    #Draw a card on Death
    def deathRattle(self):
	       player = self.getPlayer()
	       player.getHand().draw(player.getDeck())

#Representation of Elven Archer	
class ELF_ARC(Creature):
    
    def __init__(self):
        self.name = "Elvish Archer"
        self.power = 1
        self.toughness = 1
        self.maxHealth = 1
        self.cost = 1
        self.classType = "neutral"
        self.creatureType = None
        self.owner = 0
        self.tired = True
        self.board = getBoard()  
        self.screen = getScreen()
        self.buffs = []
        self.keywords = VANILLA
        if os.path.isfile(foldername+"elven_archer.png"):
            pass
        else:
            getImage("Elven%20Archer", foldername+"elven_archer.png") 
        self.img = "elven_archer.png"
        
    def copy(self):
        return ELF_ARC()
    
    def getClass(self):
        return self.classType
    
    def hasBattleCry(self):
        return True
    
    #Deal 1 Damage
    def battleCry(self):
        target = selectCard(self.img)
        dealDamage(target, 1, self.board)

#A helper function that will return the spot of a selected card.	
def selectCard(filename):	
    
    board = getBoard()
    screen = getScreen()
    
    waiting = True
    spots = board.getSpots()
    convx = screen.get_width() / 1600.0
    convy = screen.get_height() / 800.0
    while waiting:
	
    	for evnt in event.get():
    	    
    	    if evnt.type == MOUSEBUTTONDOWN:
    		mx, my = evnt.pos
            #i represents the side of the board
    		for i in range (2):
                #j represents the index of the spot
    		    for j in range(0,7):
    			     if convx*200*j < mx < convx*200*(j+1) and convy*(150 + 250*(i)) < my < convy*(150 + 250*(i+1)):
    			         square = [i,j]
    			         reversei = abs(1-i)
                         #Exit when clicked on a spot with a card in it
    			         if spots[reversei][j].getOccupied():
    				        return spots[reversei][j]
    	    drawGrid(filename)
    	    showBoard(board.getSpots())
    	    showHand(board.getHands(), getTurn())
    	    highlight((255, 255, 0), evnt.pos)
    	    display.flip()

#Apply a buff to a card currently on the fiels
def selectedBattleCry(buff, filename):	
    screen = getScreen()
    board = getBoard()
    waiting = True
    spots = board.getSpots()
    convx = screen.get_width() / 1600.0
    convy = screen.get_height() / 800.0
    while waiting:
	
        for evnt in event.get():
	    
            if evnt.type == MOUSEBUTTONDOWN:
                mx, my = evnt.pos
                for i in range (2):
                    for j in range(0,7):
                        if convx*200*j < mx < convx*200*(j+1) and convy*(150 + 250*(i)) < my < convy*(150 + 250*(i+1)):
                            square = [i,j]
                            reversei = abs(1-i)
                            if spots[reversei][j].getOccupied():
                                buff.setCreature(spots[reversei][j].getCard())
                                spots[reversei][j].getCard().addBuff(buff)
                                buff.applyBuff()
                                waiting = False
            elif evnt.type == MOUSEMOTION:
        	    drawGrid(filename)
        	    showBoard(board.getSpots())
        	    showHand(board.getHands(), getTurn())
        	    highlight((255, 255, 0), evnt.pos)
    	    display.flip()
	    

#While selecting a battle cry, highlight wherever the mouse is
def highlight(colour, pos):
    screen  = getScreen()
    convx = screen.get_width() / 1600.0
    convy = screen.get_height() / 800.0
    
    for i in range (0,10):
        if pos[1] < 100*convy and pos[0]> i*140*convx and pos[0] < (i+1)*140*convx:
            xcor = pos[0] % 140*convx
            draw.rect(screen, colour, (140*i*convx,0, 140*convx, 100*convy), 10)
        if pos[1] > 700*convy and pos[0]> i*140*convx and pos[0] < (i+1)*140*convx:
            xcor = pos[0] % 140*convx
            draw.rect(screen, colour, (140*i*convx,700*convy, 140*convx, 100*convy), 10)
    for i in range (0,7):
        if pos[1] > 200*convy and pos[1] < 400*convy and pos[0]> i*200*convx and pos[0] < (i+1)*200*convx:
            draw.rect(screen, colour, (200*i*convx,200*convy, 200*convx, 200*convy), 10)
        if pos[1] < 600*convy and pos[1] > 400*convy and pos[0]> i*200*convx and pos[0] < (i+1)*200*convx:
            draw.rect(screen, colour, (200*i*convx,400*convy, 200*convx, 200*convy), 10)
	    

    
