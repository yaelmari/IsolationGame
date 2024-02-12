def base_heuristic(game_state):
    # Get the current player
    curr_player = game_state.get_curr_player()
    # Get the number of potential moves for player 1
    game_state.set_curr_player(1)
    moves_of_player_1 = len(game_state.potential_moves())
    # Get the number of potential moves for player 2
    game_state.set_curr_player(2)
    moves_of_player_2 = len(game_state.potential_moves())
    # Set back the original player and return the difference
    game_state.set_curr_player(curr_player)
    return moves_of_player_1 - moves_of_player_2


def advanced_heuristic(game_state):
    return 0
