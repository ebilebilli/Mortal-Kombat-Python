from Chtr_design import Character
from main import round_time

def restart_system(player: Character):
    if round_time > 1 and player.hp >= 0:
        player.restart