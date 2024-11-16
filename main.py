from file_writer import txt_writer                        # fake datani file yazan kod
from fighter_list_creation import fighter_list_count      # fake datadan reader ile aldiqdan sonra liste elave eden kod
from back_settings.chrt_introduce import character_menu   # menyu fomrasinda bize fighterlari gosteren kod
from Chtr_choose_system import choose_fighter             # karakter sectiyimiz kod
from Fight_system import arena                            # doyusun bas verdiyi kod toplusu
from back_settings.messages_to_user import round_time_message                           
from round_system.configuration import RoundSystem



txt_writer()            # verilen saya gore,istenilen sayda fake datani file yazacaq.Default 40 yazacaq
fighter_list_count()    # txt write verilen saydan cox olmayaraq, istenilen sayda characteri fildan yukleyib liste elave edecek.default 15-dir
character_menu()        # charater menyusun aktiv edir ve bize gosteri

player_one = choose_fighter('player_one')      
player_two = choose_fighter('player_two')
round_time = int(input(round_time_message))

game = RoundSystem(arena, round_time, player_one, player_two)
game.start()