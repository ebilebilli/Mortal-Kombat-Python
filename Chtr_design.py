from random import randint
from back_settings.colors import Colors as clr
from back_settings.main_settings import hp_power_settings
from back_settings.main_settings import damage_power_settings
from back_settings.main_settings import ulti_power_settings

class Character:
    def __init__(self,full_name, fighter_type,start_line, end_line):
        self.full_name = full_name
        self.hp = randint(800, 1100)
        self.damage = randint(75, 100)
        self.ulti_power = randint(120, 200)
     
        self.hp_screen =  clr.GREEN_BACKGROUND + str(self.hp) + clr.COLOR_RESET
        self.damage_screen = clr.RED_BACKGROUND + str(self.damage) + clr.COLOR_RESET
        self.ulti_power_screen = clr.YELLOW_BACKGROUND + str(self.ulti_power) + clr.COLOR_RESET

        self.fighter_type = fighter_type
        self.start_line = start_line
        self.end_line = end_line

        self.ulti_mechanism = True
    def __repr__(self) -> str:
        return self.full_name

    def fight(self, attack):
        self.hp = self.hp - attack 
        self.hp_screen = clr.GREEN_BACKGROUND + str(self.hp) + clr.COLOR_RESET

    def ulti_power_offensive(self, ulti):
        self.damage = self.damage + ulti

    def ulti_power_deffensive(self, ulti):
        self.hp = self.hp + ulti

    def restart(self):
        self.hp = hp_power_settings
        self.damage = damage_power_settings
        self.ulti_power = ulti_power_settings
     
        self.hp_screen =  clr.GREEN_BACKGROUND + str(self.hp) + clr.COLOR_RESET
        self.damage_screen = clr.RED_BACKGROUND + str(self.damage) + clr.COLOR_RESET
        self.ulti_power_screen = clr.YELLOW_BACKGROUND + str(self.ulti_power) + clr.COLOR_RESET

      