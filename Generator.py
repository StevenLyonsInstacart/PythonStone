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
                        "Abusive Sergeant": ABU_SRG(self.board, self.screen), "Lance Carrier": LNC_CAR(self.board, self.screen), "Iron Beak Owl": IRN_OWL(self.board, self.screen),
                        "Elvish Archer": ELF_ARC(self.board, self.screen), "Grimscale Oracle" : GRM_MUR(self.board, self.screen), 
                        "Novice Engineer": NOV_ENG(self.board, self.screen), "Loot Hoarder": LOT_HRD(self.board, self.screen)}
        
        self.playerDict = {"Warlock" : ["guldan_portrait.jpg", WarlockPower(self.player), 'Warlock'], 
                           "Hunter" : ["rexxar_portrait.jpg", HunterPower(self.player), 'Hunter'],
                           "Warrior": ["garrosh_portrait.png", WarriorPower(self.player), 'Warrior'],
                           "Shaman": ["thrall_portrait.jpg", WarlockPower(self.player), 'Shaman'],
                           "Paladin": ["uther_portrait.png", PaladinPower(self.player, self.board), 'Paladin'],
                           "Mage": ["jaina_portrait.jpg", MagePower(self.player, self.screen, self.board), 'Mage'],
                           "Priest": ["anduin_portrait.png", PriestPower(self.player, self.screen, self.board),'Priest'],
                           "Rogue": ["valeera_portrait.png", RoguePower(self.player),'Rogue'],
                           "Druid":["malfurion_portrait.png", DruidPower(self.player), 'Druid']}
        
    def getCardDict(self):
        return self.cardDict
    def getPlayerDict(self):
        return self.playerDict