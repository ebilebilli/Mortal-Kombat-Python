from time import sleep
from back_settings.system_clear import clear_screen
from Chtr_design import Character
from arena_settings.arena_first_hp_show import starting_hp
from arena_settings.arena_first_line_check import starting_line
from arena_settings.arena_fight_system import arena_fight_system
from arena_settings.arena_ulti_system import ulti_use
from back_settings.messages_to_user import victory_message, non_victory_message

def arena(player_one: Character, player_two: Character):
    x = 0
    while True:
        if x == 0:
            starting_line(player_one, player_two)
            starting_hp(player_one, player_two)
            x += 1
        arena_fight_system(player_one, player_two)
        ulti_use(player_one)
        ulti_use(player_two)

        if player_one.hp <= 0 and player_two.hp <= 0:
            print(non_victory_message)
            break
    
        elif player_two.hp <= 0:
            print(f'{player_one.full_name} {victory_message}')
            break
          
        elif player_one.hp <= 0:
            print(f'{player_two.full_name} {victory_message}')
            break
                
        sleep(2)
        clear_screen()        