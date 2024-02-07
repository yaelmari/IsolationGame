def base_heuristic(curr_node):
    curr_game_state = curr_node.game_state
    curr_player = curr_game_state.get_curr_player()
    curr_game_state.set_curr_player(1)
    moves_of_player_1 = len(curr_game_state.potential_moves())
    curr_game_state.set_curr_player(2)
    moves_of_player_2 = len(curr_game_state.potential_moves())
    curr_game_state.set_curr_player(curr_player)
    return moves_of_player_1 - moves_of_player_2


def advanced_heuristic(curr_state):
    return 0
