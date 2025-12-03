# Recursive solution - Automata A5 - Problem 1b.

import jumpit_helpers as j
import dynamic_programming_jumpit as d
from jumpit_helpers import Game, SampleGame

# Game Instance
if int(input("Random (1) or Sample (2) game?\n> ")) == 1:
    Jump_It = Game()
else:
    Jump_It = SampleGame()

# User Feedback
j.print_board(Jump_It)

# Run function - Size must be passed explicitly for recursion
cost = j.min_cost_jumpit(Jump_It.size, Jump_It)

print(cost)