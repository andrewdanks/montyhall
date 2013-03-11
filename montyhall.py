import random, sys

class MontyHall:

    DOORS = 3

    def get_random_int(self, lower_bound, upper_bound):
        '''Want to isolate randomint method in case we want to adjust
        random algorithm.'''
        return random.randint(lower_bound, upper_bound)

    def get_random_door(self):
        return self.get_random_int(1, MontyHall.DOORS)

    def get_host_door(self, prize_door, initial_player_door):
        doors = list(range(1, MontyHall.DOORS + 1))
        for d in doors:
            if d != prize_door and d != initial_player_door:
                return d

    def log(self, message, line_breaks = 1):
        if self.verbose:
            print(message, end=line_breaks * "\n")

    def play_round(self):
        '''Return true if player would win by switching and winning; false otherwise'''

        # Put prize behind random door
        prize_door = self.get_random_door()
        self.log('Prize is behind Door %d' % prize_door)

        # Player selects random door
        initial_player_door = self.get_random_door()
        self.log('Player selects Door %d' % initial_player_door)

        # Host shows player behind random door that's not prize_door or initial_player_door:
        host_door = self.get_host_door(prize_door, initial_player_door)
        self.log('Host shows player behind Door %d' % host_door)

        return prize_door == initial_player_door

    @staticmethod
    def run(cases = 100, verbose = False):
        '''Run the simulation. Returns the switch door win percentage.'''

        simulation = MontyHall()
        simulation.verbose = verbose

        switch_and_win = 0 

        for c in range(1, cases + 1):
            simulation.log('Case %d of %d:' % (c, cases))
            switch_and_win += 1 if simulation.play_round() else 0   
            simulation.log('')

        stay_win_percentage = switch_and_win / cases
        simulation.log('Stay Win %: ' + str(round(stay_win_percentage, 5)))

        return stay_win_percentage


if __name__ == '__main__':

    if len(sys.argv) > 1:
        MontyHall.run(cases = int(sys.argv[1]), verbose = True)
    else:
        MontyHall.run(verbose = True)