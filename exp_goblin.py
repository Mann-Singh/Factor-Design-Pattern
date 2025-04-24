#second product of the expert factory
import random
from entity import Entity


class ExpGoblin(Entity):
    #creates an expert goblin with a random hp between 15 and 18 inherirts from entity
    def __init__(self):
        super().__init__("Horrible Goblin", random.randint(12, 15))
    #melee attack for the expert goblin
    def melee_attack(self, enemy):
        dmg = random.randint(5, 8)
        enemy.take_damage(dmg)
        return f"Horrible Goblin slashes {enemy.name} for {dmg} damage."
