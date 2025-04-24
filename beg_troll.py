# the second product of the beginner factory
import entity
import random

class BegTroll(entity.Entity):
  #creates a beginner troll
  def __init__(self):
    super().__init__("Beginner Troll", random.randint(8, 10))
  #method for melee attack
  def melee_attack(self, target):
    dmg = random.randint(5, 9)
    target.take_damage(dmg)
    return f"Troll smashes {target.name} for {dmg} damage."