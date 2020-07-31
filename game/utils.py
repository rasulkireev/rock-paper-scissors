def game_instructions():
    print()
    print("Let's Play!!!")
    print("Enter \"rock\",\"paper\",\"scissors\" to play")
    print()

import random
import os
import time
from messages import game_instructions

def clear():
    os.system("clear")

def get_player_info():
    name = input("Enter your First Name: ")
    age = input("Enter your age (e.g 16): ")
    gender = input("Enter your gender (m/f): ")

    return name, age, gender

def play_game(name, game_map, results_matrix):
    
    while True:
        game_instructions()
        
        # Player Move
        inp = input("Enter your move : ")
        
        if inp.lower() == "rock":
            player_move = 0
        elif inp.lower() == "paper":
            player_move = 1    
        elif inp.lower() == "scissors":
            player_move = 2
        elif inp.lower() == "exit":
            clear()
            break  
        else:
            clear()
            print("Wrong Input!!")
            game_instructions()  
            continue

        # Computer Move
        print("Computer making a move....")
        print()
        time.sleep(2)
        comp_move = random.randint(0, 2)
        print("Computer chooses ", game_map[comp_move].upper())

        # Find the winner of the match
        winner = results_matrix[player_move][comp_move]

        # Declare the winner 
        if winner == player_move:
            print(name, "WINS!!!")
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
        else:
            print("TIE GAME")

        print()
        time.sleep(2)
        clear()

# The mapping between moves and numbers
game_map = {0:"rock", 1:"paper", 2:"scissors"}
 
# Win-lose matrix for traditional game
results_matrix = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]


if __name__ == '__main__':

    name, age, gender = get_player_info()

    play_game(name, game_map, results_matrix)
