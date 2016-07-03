from card import *
from cards import *
from Player import *
from heroPower import *

class Generator():
    
    def __init__(self, screen, board, player):
        self.screen = screen
        self.board = board
        self.player = player
        self.cardDict = {"Chillwind Yeti": CH_YETI(), "Flame Juggler": FL_JUG(), "River Crocolisk": RIV_CROC(), "Murloc Raider": MUR_RAID(),
                        "Abusive Sergeant": ABU_SRG(), "Lance Carrier": LNC_CAR(), "Iron Beak Owl": IRN_OWL(),
                        "Elvish Archer": ELF_ARC(), "Grimscale Oracle" : GRM_MUR(), "Frostwolf Grunt": FRT_GRT(), 
                        "Novice Engineer": NOV_ENG(), "Loot Hoarder": LOT_HRD(), "Goldshire Footman": GLD_FOT(),
                        "Ironfur Grizzly": IRN_GRZ(), "Silverback Patriarch": SLV_PAT(), "Lord of the Arena": LRD_ARN(),
                        "Booty Bay Bodyguard": BOT_BAY(), "Sen'jin Shieldmasta": SEN_JIN(), "Stonetusk_Boar": STN_BOR(),
                        "Bluegill Warrior": BLU_WAR(), "Wolfrider": WLF_RID(), "Stormwind Knight": STR_KNT(),"Reckless Rocketeer": REK_ROC()}
        
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
        return cards