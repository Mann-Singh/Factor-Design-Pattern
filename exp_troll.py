# first product of the expert factory
import random
from entity import Entity


class ExpTroll(Entity):
  #creates an expert troll with a random hp between 15 and 18 inherirts from entity
  def __init__(self):
    super().__init__("Angry Troll", random.randint(15, 18))

  def melee_attack(self, target):
    dmg = random.randint(8, 12)
    target.take_damage(dmg)
    return f"Angry Troll smashes {target.name} for {dmg} damage."
