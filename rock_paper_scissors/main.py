from utils import instructions

# The mapping between moves and numbers
game_map = {0:"rock", 1:"paper", 2:"scissors"}
 
# Win-lose matrix for traditional game
results_matrix = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]


while True:
    welcome()

    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        clear()
        print("Wrong Choice")   
        continue
 
    # Play the traditional version of the game
    if choice == 1:
        play_game()
 
    # Quit the GAME LOOP    
    elif choice == 2:
        break
 
    # Other wrong input
    else:
        clear()
        print("Wrong choice. Read instructions carefully.")