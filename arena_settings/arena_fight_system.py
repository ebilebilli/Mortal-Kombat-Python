from Chtr_design import Character
from arena_settings.arena_dead_chtr_stngs import dead_player_hp

def arena_fight_system(player_one: Character, player_two: Character):
   
       
    player_one.fight(player_two.damage)
    print(f'{player_one.full_name} took {player_two.damage_screen} damage')
    dead_player_hp(player_one)
    print(f'{player_one.full_name} HP: {player_one.hp_screen}')
    
    player_two.fight(player_two.damage)
    print(f'{player_two.full_name} took {player_two.damage_screen} damage')
    dead_player_hp(player_two)
    print(f'{player_two.full_name} HP: {player_two.hp_screen}')

