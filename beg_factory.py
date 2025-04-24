#creates a random beginner enemy of either a goblin or a troll
import enemy_factory
import random
import beg_goblin
import beg_troll


class BeginnerFactory(enemy_factory.EnemyFactory):
    #Each time the method is called it returns a random beginner enemy
    def create_random_enemy(self):
        return random.choice([beg_goblin.BegGoblin(), beg_troll.BegTroll()])
