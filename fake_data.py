from faker import Faker
from random import choice
from back_settings.main_settings import fighter_type_one, fighter_type_two
character_info = Faker()

fighter_type =  [fighter_type_one, fighter_type_two]

class Fighter():
    def __init__(self):
        self.name = character_info.name()
        self.type = choice(fighter_type)   
        self.start_line = character_info.sentence()
        self.end_line = character_info.sentence()
        
    def __str__(self) -> str:
        return f'{self.name},{self.type},{self.start_line},{self.end_line}'
    
example = Fighter

