#All healing should be done as a method from this File

#Heal a creature by the amount specified
def healCreature(creature, amount):
    creature.setToughness(min(creature.getToughness() + amount, creature.getMaxHealth()))