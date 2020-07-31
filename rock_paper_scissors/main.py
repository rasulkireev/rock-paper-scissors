from utils import get_player_info, play_game
from messages import game_instructions

# The mapping between moves and numbers
game_map = {0:"rock", 1:"paper", 2:"scissors"}
 
# Win-lose matrix for traditional game
results_matrix = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]


if __name__ == '__main__':

    name, age, gender = get_player_info()

    play_game(name, game_map, results_matrix)
