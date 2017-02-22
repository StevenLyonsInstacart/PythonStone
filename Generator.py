from card import *
from cards import *
from Player import *
from heroPower import *

def my_cmp(a, b):
    return cmp(a.getCost(), b.getCost()) or cmp(a.getName(), b.getName())

class Generator():
    
    def __init__(self, screen, board, player):
        self.screen = screen
        self.board = board
        self.player = player
        self.cardDict = {"Flame Juggler": FL_JUG(),
                        "Abusive Sergeant": ABU_SRG(), "Lance Carrier": LNC_CAR(), "Iron Beak Owl": IRN_OWL(),
                        "Elvish Archer": ELF_ARC(), "Grimscale Oracle" : GRM_MUR(),
                        "Novice Engineer": NOV_ENG(), "Loot Hoarder": LOT_HRD(),
                        "Bluegill Warrior": BLU_WAR(), "Wolfrider": WLF_RID(), "Stormwind Knight": STR_KNT(),"Reckless Rocketeer": REK_ROC(),
                        "Argent Squire": ARG_SQU(), "Al'akir the Windlord": AL_AKIR(), "Scarlet Crusader": SCR_CRU(), "Argent Commander": ARG_COM(),
                        "Bloodfen Raptor": BLD_FEN(), "Kobold Geomancer": KBL_GEO(),
                        "Dalaran  Mage": DAL_MAG(), "Murloc Tidehunter": MUR_TID(), "Ironforge Rifleman": IRN_RFL(), "Magma Rager": MAG_RAG(),
                        "Razorfen Hunter": RAZ_HUN(), "Ogre Magi": OGR_MAG(), "Dragonling Mechanic": DRG_MEC(), "Gnomish Inventor": GNM_INV(),
                        "Malygos": MALY(), "Shattered Sun Cleric": SHT_SUN(),
                        "Raid Leader": RAD_LED(), "Stormpike Commando": STR_COM(), "Archmage": ARCH(),
                        "Nightblade": NGT_BLD(), "Frostwolf Warlord": FRT_WAR(), "Darkscale Healer": DRK_HEL(), "Gurubashi Berserker": GUR_BER(),
                        "Stormwind Champion": STR_CHM(), "Starfire": STR_FIR()}
    
        db = MySQLdb.connect("localhost","root","root","sys" )
        cursor = db.cursor()
        cursor.execute("SELECT count(*) FROM sys.minion")
        entries = cursor.fetchone()
        db.close()
        for i in range(entries[0]):
            newCard = makeCreature(i+1)
            self.cardDict[newCard.getName()] = newCard
        
        self.playerDict = {"Warlock" : ["guldan_portrait.jpg", WarlockPower(self.player), 'Warlock'], 
                           "Hunter" : ["rexxar_portrait.jpg", HunterPower(self.player), 'Hunter'],
                           "Warrior": ["garrosh_portrait.png", WarriorPower(self.player), 'Warrior'],
                           "Shaman": ["thrall_portrait.jpg", WarlockPower(self.player), 'Shaman'],
                           "Paladin": ["uther_portrait.png", PaladinPower(self.player), 'Paladin'],
                           "Mage": ["jaina_portrait.jpg", MagePower(self.player), 'Mage'],
                           "Priest": ["anduin_portrait.png", PriestPower(self.player),'Priest'],
                           "Rogue": ["valeera_portrait.png", RoguePower(self.player),'Rogue'],
                           "Druid":["malfurion_portrait.png", DruidPower(self.player), 'Druid']}
        
    def getCardDict(self):
        return self.cardDict
    def getPlayerDict(self):
        return self.playerDict
    def getCard(self, name):
        return self.cardDict[name].copy()
    def getCards(self):
        names = self.cardDict.keys()
        cards = []
        for i in names:
            cards.append(self.getCard(i))
        print cards
        cards.sort(my_cmp)
        print cards
        return cards
    
def skim(player, cards):
    newList = []
    for card in cards:
        if card.getClass()== "neutral" or card.getClass() == player.getRole():
            newList.append(card)
    return newList
        