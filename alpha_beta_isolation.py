import math


class AlphaBetaNode:
    def __init__(self, v, a, b, parent, game_state, create_children=True):
        self.parent = parent
        self.v = v
        self.a = a
        self.b = b
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
        self.game_state = game_state
        if create_children:
            self.children = game_state.get_moves()
        self.curr_child = 0
        self.best_child = None

    def update_a(self):
        self.a = max(self.a, self.v)

    def update_b(self):
        self.b = min(self.b, self.v)

    def update_v_as_max(self):
        child = self.children[self.curr_child - 1]
        new_v = child.v
        if new_v > self.v:  # curr child is a AlphaBetaNode
            self.best_child = child
            self.v = new_v
            return True
        return False

    def update_v_as_min(self):
        child = self.children[self.curr_child - 1]
        new_v = child.v
        if new_v < self.v:
            self.best_child = child
            self.v = new_v
            return True
        return False

    def update_my_v(self, new_v, am_i_max):
        if am_i_max:
            if new_v > self.v:
                self.v = new_v

        else:
            if new_v < self.v:
                self.v = new_v

    def should_we_prun(self):
        return self.a >= self.b

    def update_v_in_the_parent(self, am_i_max):
        if self.parent is not None:
            # Check if there are available children
            if self.parent.curr_child < len(self.parent.children):
                if am_i_max:
                    self.parent.update_v_as_min()
                else:
                    self.parent.update_v_as_max()
            else:
                self.parent.update_v_in_the_parent(not am_i_max)

    def get_next_child(self, am_i_max, create_children=True):
        # Check if there are available children
        if self.curr_child < len(self.children):
            self.curr_child += 1
            if am_i_max:
                v = math.inf
            else:
                v = -math.inf
            curr_move = self.children[self.curr_child - 1]
            self.children[self.curr_child - 1] = AlphaBetaNode(v, self.a, self.b, self, curr_move, create_children)
            return self.children[self.curr_child - 1]
        return None


root = None


def alphabeta_max(current_game):
    global root
    if root is None:
        root = AlphaBetaNode(-math.inf, -math.inf, math.inf, None, current_game)  # (v, a, b, parent, gameState)
        maximin(root)
    parents_v = root.v
    root = root.best_child
    root.parent = None
    return parents_v, root.game_state


def alphabeta_min(current_game):
    global root
    if root is None:
        root = AlphaBetaNode(math.inf, -math.inf, math.inf, None, current_game)  # (v, a, b, parent, gameState)
        minimax(root)
    parents_v = root.v
    root = root.best_child
    root.parent = None
    return parents_v, root.game_state


def maximin(current_node):
    if current_node.game_state.is_terminal():
        score = current_node.game_state.get_score()
        current_node.update_my_v(score, True)
        return
    best = None
    move = current_node.get_next_child(True)
    while move is not None:
        minimax(move)
        if current_node.update_v_as_max():
            best = current_node
        current_node.update_a()
        if current_node.should_we_prun():
            return current_node.v, None
        move = current_node.get_next_child(True)
    return current_node.v, best


def minimax(current_node):
    if current_node.game_state.is_terminal():
        score = current_node.game_state.get_score()
        current_node.update_my_v(score, False)
        return
    best = None
    move = current_node.get_next_child(False)
    while move is not None:
        maximin(move)
        if current_node.update_v_as_min():
            best = current_node

        current_node.update_b()
        if current_node.should_we_prun():
            return current_node.v, None
        move = current_node.get_next_child(False)
    return current_node.v, best
