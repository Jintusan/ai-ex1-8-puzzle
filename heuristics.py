# ============================================================
# heuristics.py
# Heuristic functions for the 8-puzzle.
# Both estimate the number of moves still needed to reach the goal
# and never overestimate it (admissible).
# ============================================================

from state import GOAL

# Goal position of every tile, e.g. GOAL_POSITION[7] = 7
# (calculated once, so we don't have to search the goal every time)
GOAL_POSITION = {tile: index for index, tile in enumerate(GOAL)}


def hamming(state):
    """
    Input:    state - tuple of 9 numbers (0 = empty field)
    Output:   number of tiles that are not on their goal position
    Function: Heuristic h1 (misplaced tiles). The empty field is not counted.
    """
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
    return count


def manhattan(state):
    """
    Input:    state - tuple of 9 numbers (0 = empty field)
    Output:   sum of the Manhattan distances of all tiles to their goal positions
    Function: Heuristic h2. For every tile: |row difference| + |column difference|.
              The empty field is not counted.
    """
    total = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue                                   # skip the empty field
        row, col = divmod(i, 3)                        # current position
        goal_row, goal_col = divmod(GOAL_POSITION[tile], 3)   # goal position
        total += abs(row - goal_row) + abs(col - goal_col)
    return total


# ------------------------------------------------------------
# Tests: only run when this file is started directly
# ------------------------------------------------------------
if __name__ == "__main__":
    from state import random_state, successors

    start = (7, 2, 4, 5, 0, 6, 8, 3, 1)
    print("Start state from the slides: hamming =", hamming(start),
          ", manhattan =", manhattan(start))

    print("Goal state: hamming =", hamming(GOAL),
          ", manhattan =", manhattan(GOAL))

    one_move = successors(GOAL)[0]   # one move away from the goal
    print("One move from the goal: hamming =", hamming(one_move),
          ", manhattan =", manhattan(one_move))

    # Manhattan should always be >= Hamming
    ok = True
    for _ in range(1000):
        s = random_state()
        if manhattan(s) < hamming(s):
            ok = False
    print("Manhattan >= Hamming for 1000 random states:", ok)
