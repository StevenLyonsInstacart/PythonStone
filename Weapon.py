class Weapon():
    
    def __init__(self, name, power, durability, image):
        self.name = name
        self.power = power
        self.durability = durability
        self.image = image
        
    def getName(self):
        return self.name
    def getPower(self):
        return self.power
    def getDurability(self):
        return self.durability
    
    def setName(self, name):
        self.name = name
    def setPower(self, power):
        self.power = power
    def setDurability(self, durability):
        self.durability = durability
        
    def attackCheck(self):
        self.durability -= 1
        return self.durability < 1
        
        
class Dagger(Weapon):
    
    def __init__(self):
        Weapon.__init__(self, "Dagger", 1, 2, "daggers.png")