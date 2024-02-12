import math


def alphabeta_max(current_game):
    return maximin(current_game, -math.inf, math.inf)


def alphabeta_min(current_game):
    return minimax(current_game, -math.inf, math.inf)


def maximin(current_game, a, b):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, a, b)
        if v < mx:
            v = mx
            best_move = move
        # update a
        a = max(a, v)
        # check if we should prun
        if a >= b:
            break
    return v, best_move


def minimax(current_game, a, b):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, a, b)
        if v > mx:
            v = mx
            best_move = move
        # update b
        b = min(b, v)
        # check if we should prun
        if a >= b:
            break
    return v, best_move
