# extends the entity class to create a hero object
import random
from entity import Entity

class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, 50)  # Default HP
    # melee attack for the hero
    def melee_attack(self, target):
        dmg = random.randint(1, 6) + random.randint(1, 6)
        target.take_damage(dmg)
        return f"{self.name} slashes a {target.name} with a sword for {dmg} damage."
    # ranged attack for the hero
    def ranged_attack(self, enemy):
        dmg = random.randint(1, 12)
        enemy.take_damage(dmg)
        return f"{self.name} pierces a {enemy.name} with an arrow for {dmg} damage."