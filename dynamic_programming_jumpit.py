from Game import Game
def min_cost_jump_it(game: Game):
    target = game.size

    # Min cost to a given column and path tracking
    min_to_col = [float("inf")] * game.size
    path = [[] for _ in range(game.size)]

    # Base Case
    min_to_col[0] = game.costs[0]
    path[0] = [1]

    # If there is more than 1 element, loop through the rest filling in min_to_col table
    for cur_col in range(1, game.size):
        # Which columns could have reached cur_col?
        for prev_col in range(max(0, cur_col - 3), cur_col):
            # Can the prev_col jump far enough to reach cur_col?
            if prev_col + game.jumps[prev_col] >= cur_col:
                # What does it cost this prev_col to be used to jump to cur_col?
                cost_from_col = min_to_col[prev_col] + game.costs[cur_col]

                # Update if the cost_from_col is better than whatever we currently have
                if cost_from_col < min_to_col[cur_col]:
                    min_to_col[cur_col] = cost_from_col
                    path[cur_col] = path[prev_col] + [cur_col + 1]

    return min_to_col[target - 1], path[target - 1]