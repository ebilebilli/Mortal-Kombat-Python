from random import choice
from time import sleep

from fighter_list_creation import fighters_list
from back_settings.main_settings import random_type_words
from back_settings.messages_to_user import system_choose
from back_settings.messages_to_user import character_choose_message


def choose_fighter(player_name: str):
    player_choice = input(f'{player_name}{character_choose_message}').title().strip()

    for fighter in fighters_list:
        if fighter.full_name == player_choice:
            return fighter

        elif player_choice in random_type_words:
            random_choose = choice(fighters_list)
            print(f'{player_name} choose: {random_choose.full_name}')
            sleep(1.1)
            return random_choose

        else:
            random_choose = choice(fighters_list)
            print(f'{system_choose} {player_name} choose: {random_choose.full_name}')
            return random_choose

