from Board import *
from Constants import *


def battleCry1():
        enemy = getBoard().getEnemyPlayer()
        if enemy.isArmed():
            enemy.setWeapon(None)
            
def battleCry2():
        target = selectCard("pics/voodoo_doctor.png")
        if target.getType() == "Spot":
            healCreature(target.getCard(), 2)
        else:
            target.heal(2)
            
def getBCs ():
    return [None, battleCry1, battleCry2]