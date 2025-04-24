#parent for the factory classes
import abc

class EnemyFactory(abc.ABC):
    
    @abc.abstractmethod
    #Base method for creating a random enemy which the factories implement
    def create_random_enemy(self):
        pass
   