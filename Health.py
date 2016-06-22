def healCreature(creature, amount):
    creature.setToughness(min(creature.getToughness() + amount, creature.getMaxHealth()))