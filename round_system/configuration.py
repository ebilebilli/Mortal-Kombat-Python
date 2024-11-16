class RoundSystem:
    def __init__(self, arena_func, rounds, player_one, player_two):
        self.arena_func = arena_func
        self.rounds = max(1, rounds)  
        self.player_one = player_one
        self.player_two = player_two

    def start(self):
        for round in range(1, self.rounds + 1):
            print(f'--- Round {round} started ---')
            self.arena_func(self.player_one, self.player_two) 
            self.reset_players()  

        print('---Round is over---')

    def reset_players(self):
        self.player_one.restart()
        self.player_two.restart()
