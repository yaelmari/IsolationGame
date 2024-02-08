import math
from alpha_beta_isolation import AlphaBetaNode

h = None

root = None


def alphabeta_max_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    global root
    if root is None:
        root = AlphaBetaNode(-math.inf, -math.inf, math.inf, None,
                             current_game)  # (v, a, b, parent, gameState)
    else:
        root = AlphaBetaNode(-math.inf, -math.inf, math.inf, None,
                             root.game_state)  # (v, a, b, parent, gameState)
    maximin(root, depth)
    parents_v = root.v
    root = root.best_child
    return parents_v, root.game_state


def alphabeta_min_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    global root
    if root is None:
        root = AlphaBetaNode(math.inf, -math.inf, math.inf, None,
                             current_game)  # (v, a, b, parent, gameState)
    else:
        root = AlphaBetaNode(math.inf, -math.inf, math.inf, None,
                             root.game_state)  # (v, a, b, parent, gameState)
    minimax(root, depth)
    parents_v = root.v
    root = root.best_child

    return parents_v, root.game_state


def maximin(current_node, depth):
    global h
    if current_node.game_state.is_terminal():
        score = current_node.game_state.get_score()
        current_node.update_my_v(score, True)
        current_node.update_a()
        return
    if depth == 0:
        h1 = h(current_node)
        if current_node.update_my_v(h1, True):
            best = current_node
        current_node.update_a()
        return current_node.v, None
    best = None
    move = current_node.get_next_child(True, depth > 1)
    while move is not None:
        minimax(move, depth - 1)
        if current_node.update_v_as_max():
            best = current_node
        current_node.update_a()
        if current_node.should_we_prun():
            return current_node.v, None
        move = current_node.get_next_child(True, depth > 1)
    return current_node.v, best


def minimax(current_node, depth):
    global h
    if current_node.game_state.is_terminal():
        score = current_node.game_state.get_score()
        current_node.update_my_v(score, False)
        current_node.update_b()
        return current_node.v, None
    if depth == 0:
        h1 = h(current_node)
        if current_node.update_my_v(h1, False):
            best = current_node
        current_node.update_b()
        return current_node.v, None
    best = None
    move = current_node.get_next_child(False, depth > 1)
    while move is not None:
        maximin(move, depth - 1)
        if current_node.update_v_as_min():
            best = current_node
        current_node.update_b()
        if current_node.should_we_prun():
            return current_node.v, None
        move = current_node.get_next_child(False, depth > 1)
    return current_node.v, best
