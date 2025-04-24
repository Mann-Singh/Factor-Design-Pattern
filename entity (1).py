import abc
class Entity:
  #class for entity object, assigning a name, and a maxhp, sets method for taking damage and a string method to print
  def __init__(self, name, max_hp):
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp
    

  @property
  #returns the name
  def name(self):
    return self._name

  @property
  #returns the hp
  def hp(self):
    return self._hp
  #reduces hp after the entity takes an attack
  def take_damage(self, dmg):
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0
    return self._hp
  #prints the name and hp of the entity
  def __str__(self):
    return self._name + ": " + str(self.hp) + "/" + str(self._max_hp)
  #abstract method for melee attack
  @abc.abstractmethod
  def melee_attack(self, target) -> str:
    pass
    