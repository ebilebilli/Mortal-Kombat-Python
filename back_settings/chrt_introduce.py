from fighter_list_creation import fighters_list
def character_menu():
    for fighter in fighters_list:
        print(f'Name: {fighter.full_name} Hp: {fighter.hp_screen} Damage: {fighter.damage_screen} Ulti Power: {fighter.ulti_power_screen} Type: {fighter.fighter_type}')

if __name__ == '__main__':
    character_menu()
