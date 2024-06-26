import numpy as np
import minimax_isolation
import alpha_beta_isolation, heuristic_alpha_beta_isolation, heuristics
from game_state import game_state
from player_agent import player_agent, player_agent_heuristics
from time import time


def print_current_state(curr_state, player_turn):
    print(f"Current player is player {player_turn},"
          f" moved to {curr_state.get_player_locations()[player_turn]}."
          f"\nThe board is:\n"
          f"{curr_state.get_grid()}")

i = 0
def play_isolation(player_1, player_2, init_state):
    global i
    players = {1: player_1, 2: player_2}
    curr_state = init_state
    player_turn = curr_state.get_curr_player()
    curr_player = players[player_turn]
    print(f"start board is:\n{curr_state.get_grid()}")
    while not curr_state.is_terminal():
        chosen_move = curr_player.get_next_move(curr_state)
        curr_state.apply_move(chosen_move)
        # print_current_state(curr_state, player_turn)
        print(f"turn {i}")
        i+=1
        player_turn = curr_state.get_curr_player()
        curr_player = players[player_turn]
    print(f"\n\nPlayer {(player_turn % 2) + 1} is the winner!!")


def play_with_minimax():
    player_1 = player_agent(minimax_isolation.maximin)
    player_2 = player_agent(minimax_isolation.minimax)
    grid = np.zeros((3, 3), dtype=int)
    init_state = game_state(grid, (0, 0), (2, 2), 1)
    play_isolation(player_1, player_2, init_state)


def play_with_alpha_beta():
    player_1 = player_agent(alpha_beta_isolation.alphabeta_max)
    player_2 = player_agent(alpha_beta_isolation.alphabeta_min)
    grid = np.zeros((4, 4), dtype=int)
    init_state = game_state(grid, (0, 0), (3, 3), 1)
    play_isolation(player_1, player_2, init_state)


def play_with_heuristics():
    # depth_player_1 = 3
    # depth_player_2 = 3

    # try different depths, you can change the depth numbers, board size and locations
    # depth_player_1 = 6
    # depth_player_2 = 1

    depth_player_1 = 4
    depth_player_2 = 4

    player_1 = player_agent_heuristics(heuristic_alpha_beta_isolation.alphabeta_max_h, heuristics.base_heuristic,
                                       depth_player_1)
    player_2 = player_agent_heuristics(heuristic_alpha_beta_isolation.alphabeta_min_h, heuristics.base_heuristic,
                                       depth_player_2)
    grid = np.zeros((7, 7), dtype=int)
    init_state = game_state(grid, (0, 0), (6, 6), 1)
    play_isolation(player_1, player_2, init_state)


def play_with_advanced_heuristics():
    # depth_player_1 = 3
    # depth_player_2 = 3
    depth_player_1 = 5
    depth_player_2 = 5


    #Does player 1 wins most of the games you play?
    player_1 = player_agent_heuristics(heuristic_alpha_beta_isolation.alphabeta_max_h, heuristics.advanced_heuristic,
                                       depth_player_1)
    player_2 = player_agent_heuristics(heuristic_alpha_beta_isolation.alphabeta_min_h, heuristics.base_heuristic,
                                       depth_player_2)
    grid = np.zeros((7, 7), dtype=int)
    init_state = game_state(grid, (0, 0), (6, 6), 1)
    play_isolation(player_1, player_2, init_state)


if __name__ == '__main__':
    start = time()
    # play_with_minimax()
    # play_with_alpha_beta()
    # play_with_heuristics()
    # end = time()
    #
    # print(f"the time is: {end - start} ms")
    start1 = time()

    # play_with_heuristics()
    play_with_advanced_heuristics()
    end1 = time()

    print(f"the time is: {end1 - start1} ms")
    # play_with_advanced_heuristics()