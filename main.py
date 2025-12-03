# Recursive solution - Automata A5 - Problem 1b.

import jumpit_helpers as j
import dynamic_programming_jumpit as d
from Game import Game, SampleGame
from JumpItController import Controller

# User Interface Controller
Ctl = Controller()

# Game Instance
match Ctl.get_user_inp_game_type():
    case "Sample":
        Jump_It = SampleGame()
    case _:
        Jump_It = Game()

# User Feedback
j.print_board(Jump_It)

# Run function - Size must be passed explicitly for recursion
match Ctl.get_user_inp_alg_type():
    case "Recursive Programming":
        cost = j.min_cost_jump_it(Jump_It.size, Jump_It)
    case _:
        cost = d.min_cost_jump_it(Jump_It)

print(f"Result: {cost}")
