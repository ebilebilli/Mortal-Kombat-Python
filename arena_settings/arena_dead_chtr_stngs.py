from Chtr_design import Character
from back_settings.colors import Colors as clr

def dead_player_hp(player: Character):
    zero_hp = clr.GREEN_BACKGROUND + str(0) + clr.COLOR_RESET
    if player.hp <= 0:
        player.hp_screen = zero_hp
