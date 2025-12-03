import random as rnd
from tabulate import tabulate as tab
from enum import Enum

#####################################################################
""" $$$$$$$$$$$$$$$$$$$$$$$$$ CLASSES $$$$$$$$$$$$$$$$$$$$$$$$$$$ """
#####################################################################

""" ######################## Game Class ######################### """
class Game:
    def __init__(self):
        self.size = 5  # init_game_size_from_user()
        self.board = create_board(self.size)

class Sample_Game(Game):
    def __init__(self):
        # No super since we are overwriting everything
        self._sample = int(init_sample_choice_from_user())
        self.board = get_sample_board(choice=self._sample)
        self.size = get_size_from_board(self.board)

#####################################################################
""" $$$$$$$$$$$$$$$$$$$$$$$$ Functions $$$$$$$$$$$$$$$$$$$$$$$$$$ """
#####################################################################

""" ######################## GAME FUNCS ######################### """
# Get User Input
def init_game_size_from_user():
    return int(input("Please enter an integer for the size of the JumpIt gameboard: "))

def init_sample_choice_from_user():
    return int(input("Which sample board would you like to use? (hint: choices are 1-5): "))

# Create the game board
def create_board(n: int):
    board = [
        [],
        [],
    ]
    for col in range(n):
        # Rand cost
        cost = rnd.randint(1, 100)
        # Rand jump val (within given range)
        jump = rnd.randint(1, 3)

        # Add the data to the board
        board[0].append(cost)
        board[1].append(jump)
    return board


""" ######################### UTILITIES ######################### """
# Print out the board (zip used to transpose data)
def print_board(instance: Game):
    headers = [str(i) for i in range(1, instance.size + 1)]

    print(
        tab(
            tabular_data=instance.board,
            tablefmt="fancy_grid",
            headers=headers,
            showindex=["Cost", "Jump"]
        )
    )

def get_sample_board(choice: int) -> list:
    match choice:
        case 1:
            return Sample.ONE.value
        case 2:
            return Sample.TWO.value
        case _:
            return Sample.THREE.value

def get_size_from_board(board: list):
    return len(board[0])

""" ######################## ALGORITHMS ######################### """
# Recursive (Naive) Solution - Dynamic Programming Problem
def min_cost_jumpit(instance: Game):
    cost = instance.board[0][0]
    jump = instance.board[0][1]


""" ########################### ENUMS ############################ """
class Sample(Enum):
    ONE = [
        [ 1,  5,  5, 50, 20 ],
        [ 1,  2,  2,  2,  3 ],
    ]
    TWO = [
        [ 1, 75, 54, 10, 54, 10, 27, 10, 20 ],
        [ 2,  2,  3,  1,  3,  1,  3,  1,  3 ],
    ]
    THREE = [
        [ 1,  5,  5, 50, 20,  1,  5,  5, 50, 20, 98,  5, 35, 50, 20 ],
        [ 1,  2,  2,  2,  3,  1,  2,  3,  2,  3,  1,  2,  2,  2,  3 ],
    ]