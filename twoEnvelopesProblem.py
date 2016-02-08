import random

# there are two strategies:
# 1) leave the envelope as it is
# 2) exchange it

# file:
# player_name; experiment_description; wins; total money gain
# experiment_description:
# the number of iterations; strategy_description


class Statistics:
    def __init__(self, total_sum=0, wins=0):
        self.total_sum = total_sum
        self.wins = wins

    def change_stat(self, sum_, win):
        self.total_sum += sum_
        if win != 0:
            self.wins += win

    def reset_values(self):
        self.total_sum = 0
        self.wins = 0


class Player:
    def __init__(self, name="player", sum_in_env=0):
        self.name = name
        self.sum_in_env = sum_in_env
        self.stat = Statistics()

    # changes the statistics on the total gain
    # and on the amount of wins
    def change_stat(self, win):
        self.stat.change_stat(self.sum_in_env, win)

    # reset the statistics
    def reset_stat(self):
        self.stat.reset_values()

    # prints the statistics
    def print_stat(self):
        print(self.name + ";" + str(self.stat.total_sum) + ";" + str(self.stat.wins))


# integer number generator in range from 1 to 100000
class Generator:
    def __init__(self):
        pass

    @staticmethod
    def generate(player1, player2):
        value = random.randint(1, 100000)
        if value % 2:
            player1.sum_in_env = value
            player2.sum_in_env = 2 * value
        else:
            player2.sum_in_env = value
            player1.sum_in_env = 2 * value


class Game:
    def __init__(self):
        pass

    # 'play' function, conducts the experiment given amount of times and under
    # chosen strategy
    @staticmethod
    def play(experiment, strategy, num_of_iterations, player1, player2):
        player1.reset_stat()
        player2.reset_stat()
        for i in range(0, num_of_iterations):
            Generator.generate(player1, player2)
            if strategy == 2:
                Game.swap_sums_in_env(player1, player2)
            Game.chose_the_winner(player1, player2)
        Game.print_statistics(experiment, strategy, num_of_iterations, player1, player2)

    @staticmethod
    def swap_sums_in_env(player1, player2):
        temp = player1.sum_in_env
        player1.sum_in_env = player2.sum_in_env
        player2.sum_in_env = temp

    @staticmethod
    def chose_the_winner(player1, player2):
        if player1.sum_in_env > player2.sum_in_env:
            player1.change_stat(1)
            player2.change_stat(0)
        else:
            player2.change_stat(1)
            player1.change_stat(0)

    @staticmethod
    def check_file():
        try:
            file_ = open("game_stat.csv", "r")
            file_.close()
            return True
        except IOError:
            return False

    @staticmethod
    def print_statistics(experiment, strategy, num_of_iterations, player1, player2):
        created = Game.check_file()
        try:
            file_ = open("game_stat.csv", "a+")
        except IOError:
            print("Could not open the file!")
            return
        if created is False:
            file_.write("experiment;strategy;iterations;player1.wins;player1.total_sum;player2.wins;player2.total_sum;\n")
        file_.write(str(experiment) + ";" + str(strategy) + ";" + str(num_of_iterations) + ";" +
                    str(player1.stat.wins) + ";" + str(player1.stat.total_sum) + ";" +
                    str(player2.stat.wins) + ";" + str(player2.stat.total_sum) + "\n")
        file_.flush()
        file_.close()


def main():
    player1 = Player()
    player2 = Player()

    Game.play(1, 1, 10, player1, player2)
    Game.play(2, 2, 10, player1, player2)
    Game.play(3, 1, 100, player1, player2)
    Game.play(4, 2, 100, player1, player2)
    Game.play(5, 1, 1000, player1, player2)
    Game.play(6, 2, 1000, player1, player2)
    Game.play(7, 1, 10000, player1, player2)
    Game.play(8, 2, 10000, player1, player2)
    Game.play(9, 1, 100000, player1, player2)
    Game.play(10, 2, 100000, player1, player2)
    Game.play(11, 1, 1000000, player1, player2)
    Game.play(12, 2, 1000000, player1, player2)

main()
