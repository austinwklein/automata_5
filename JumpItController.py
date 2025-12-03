class Controller:
    @staticmethod
    def get_user_inp_game_type() -> str:
        choice_map = {
            1: "Sample",
            2: "Random",
        }
        choice = int(input(
            "Choose Game Type: \n"
            "(1) Sample Board \n"
            "(2) Random Board \n"
            " >  "
        ))
        # Defaults to "Random" if invalid options are input
        return choice_map.get(choice, "Random")

    @staticmethod
    def get_user_inp_alg_type() -> str:
        choice_map = {
            1: "Recursive Programming",
            2: "Dynamic Programming",
        }
        choice = int(input(
            "Choose Algorithm Type: \n"
            "(1) Recursive Programming \n"
            "(2) Dynamic Programming \n"
            " >  "
        ))
        # Defaults to "Dynamic Programming" if invalid options are input
        return choice_map.get(choice, "Dynamic Programming")