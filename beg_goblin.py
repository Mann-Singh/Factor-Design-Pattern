# the first 'product' of the beginner factory
import entity
import random

class BegGoblin(entity.Entity):
  #creates a beginner goblin with a random hp between 7 and 9
  def __init__(self):
    super().__init__("Beginner Goblin", random.randint(7, 9))
  #melee attack for the beginner goblin
  def melee_attack(self, target):
    dmg = random.randint(4, 6)
    target.take_damage(dmg)
    return f"Goblin smashes {target.name} for {dmg} damage."