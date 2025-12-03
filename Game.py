import jumpit_helpers as j
""" ######################## Game Class ######################### """
class Game:
    def __init__(self):
        self.size = j.init_game_size_from_user()
        self.board = j.create_board(self.size)
        self.costs = self.board[0]
        self.jumps = self.board[1]

class SampleGame(Game):
    def __init__(self):
        # No super since we are overwriting everything
        self._sample = int(j.init_sample_choice_from_user())
        self.board = j.get_sample_board(choice=self._sample)
        self.size = j.get_size_from_board(self.board)
        self.costs = self.board[0]
        self.jumps = self.board[1]