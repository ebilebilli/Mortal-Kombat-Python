from Chtr_design import Character
from time import sleep

def starting_line(player_one: Character, player_two: Character):
        print(f'{player_one.full_name} VS {player_two.full_name}') 
        print(f'{player_one.full_name}: {player_one.start_line}')
        sleep(2)
        print(f'{player_two.full_name}: {player_two.start_line}')
        sleep(2)
 

