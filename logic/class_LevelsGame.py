from pygame.math import lerp

class LevelsGame:
    __instance = None
    
    __levels_dict = {
        'player_level': 1,
        'game_level': 1,
        'current_level': 1,
        'attack_level': 2,
        'final_level': 5,
        'enemies_min': 7,
        'enemies_max': 20,
        
    }
    
    
    
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.__dict__ = self.__levels_dict
        self.enemies = round(lerp(self.enemies_min, self.enemies_max, self.attack_level / self.final_level))