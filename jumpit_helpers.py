import random as rnd
from tabulate import tabulate as tab
from enum import Enum
from Game import Game

""" ######################## GAME FUNCS ######################### """
# Get User Input
def init_game_size_from_user():
    return int(input("Please enter an integer for the size of the JumpIt gameboard: "))

def init_sample_choice_from_user():
    return int(input("Which sample board would you like to use? (hint: choices are 1-3): "))

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

def get_cost(column: int, g: Game) -> int:
    return g.board[0][column - 1]  # Index vs Col

""" ######################## ALGORITHMS ######################### """
# Recursive (Naive) Solution - Dynamic Programming Problem
def min_cost_jump_it(col: int, instance: Game):
    if col == 1:
        return get_cost(col, instance), [1]

    min_cost = float("inf")
    best_path = []

    for given_col in range(max(1, col - 3), col):  # Last three since max jump is three
        if given_col + instance.jumps[given_col - 1] >= col:
            cost_from_prev, path_from_prev = min_cost_jump_it(given_col, instance)
            cost_to_here = cost_from_prev + instance.costs[col - 1]

            if cost_to_here < min_cost:
                min_cost = cost_to_here
                best_path = path_from_prev + [col]

    return min_cost, best_path


""" ########################### ENUMS ############################ """
class Sample(Enum):
    ONE = [
        [ 10,  3, 87, 58, 57, 10 ],
        [  1,  2,  3,  1,  1,  1 ],
    ]
    TWO = [
        [ 1, 75, 54, 10, 54, 10, 27, 10, 20 ],
        [ 2,  2,  3,  1,  3,  1,  3,  1,  3 ],
    ]
    THREE = [
        [ 1,  5,  5, 50, 20,  1,  5,  5, 50, 20, 98,  5, 35, 50, 20 ],
        [ 1,  2,  2,  2,  3,  1,  2,  3,  2,  3,  1,  2,  2,  2,  3 ],
    ]