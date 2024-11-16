from Chtr_design import Character
from back_settings.main_settings import fighter_type_one, fighter_type_two, ulti_line
from back_settings.messages_to_user import damage_ulti_message, healing_ulti_message


def ulti_use(player: Character):
    conditon_one = (player.hp <= ulti_line and player.fighter_type == fighter_type_one and player.ulti_mechanism is True)
    conditon_two = (player.hp <= ulti_line and player.fighter_type == fighter_type_two and player.ulti_mechanism is True)
    if conditon_one:
        player.ulti_power_offensive(player.ulti_power)
        print(f'{player.full_name} used:>> {player.ulti_power_screen} {damage_ulti_message}')
        player.ulti_mechanism = False
    
    elif conditon_two:
        player.ulti_power_deffensive(player.ulti_power)
        print(f'{player.full_name} used:>> {player.ulti_power_screen} {healing_ulti_message}')
        player.ulti_mechanism = False
        



