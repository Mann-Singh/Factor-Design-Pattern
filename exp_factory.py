#factory for the expert enemies creates a random enemy of either a goblin or a troll
import random
from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll


class ExpertFactory(EnemyFactory):
    ##Each time the method is called it returns a random expert enemy
    def create_random_enemy(self):
        return random.choice([ExpGoblin(), ExpTroll()])
