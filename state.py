# ============================================================
# state.py
# Representation of the 8-puzzle, move generation,
# random start states and solvability check
# ============================================================

import random

# Goal state: empty field (0) top left, then 1 to 8
GOAL = (0, 1, 2, 3, 4, 5, 6, 7, 8)


def successors(state):
    """
    Input:    state - tuple of 9 numbers (0 = empty field), read row by row
    Output:   list of all states reachable with exactly one move
    Function: Moves the empty field up, down, left or right,
              as long as it stays inside the 3x3 grid.
    """
    result = []
    empty = state.index(0)              # position of the empty field (0 to 8)
    row, col = divmod(empty, 3)         # position -> row and column

    # The four directions: (row change, column change)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:          # still inside the grid?
            new = list(state)                               # changeable copy
            swap = new_row * 3 + new_col                    # row, column -> position
            new[empty], new[swap] = new[swap], new[empty]   # swap the two fields
            result.append(tuple(new))
    return result


def show(state):
    """
    Input:    state - tuple of 9 numbers
    Output:   none (prints the puzzle to the terminal)
    Function: Prints the state as a 3x3 grid, the empty field as _
    """
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


def inversions(state):
    """
    Input:    state - tuple of 9 numbers (0 = empty field)
    Output:   number of inversions (integer)
    Function: Counts all pairs where a bigger number comes before
              a smaller one. The empty field (0) is ignored.
    """
    numbers = [x for x in state if x != 0]   # leave out the 0
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # only numbers further back
            if numbers[i] > numbers[j]:
                count += 1
    return count


def is_solvable(state):
    """
    Input:    state - tuple of 9 numbers
    Output:   True if the state is solvable, otherwise False
    Function: A state is solvable if its number of inversions has the
              same parity (even/odd) as the goal state.
    """
    return inversions(state) % 2 == inversions(GOAL) % 2


def random_state():
    """
    Input:    none
    Output:   a random, solvable state (not equal to the goal)
    Function: Shuffles the numbers 0-8 until the result is solvable.
    """
    while True:
        numbers = list(range(9))    # [0, 1, 2, ..., 8]
        random.shuffle(numbers)     # shuffle randomly
        state = tuple(numbers)
        if is_solvable(state) and state != GOAL:
            return state


# ------------------------------------------------------------
# Tests: only run when this file is started directly
# ------------------------------------------------------------
if __name__ == "__main__":
    start = (7, 2, 4, 5, 0, 6, 8, 3, 1)

    print("Start state from the slides:")
    show(start)

    print("Successors:")
    for s in successors(start):
        show(s)

    print("Number of successors of the goal:", len(successors(GOAL)))

    print("Start state:", inversions(start), "inversions, solvable:", is_solvable(start))

    swapped = (0, 2, 1, 3, 4, 5, 6, 7, 8)   # goal with 1 and 2 swapped
    print("1 and 2 swapped:", inversions(swapped), "inversions, solvable:", is_solvable(swapped))

    print("\nA random solvable puzzle:")
    show(random_state())

    # How many completely random arrangements are solvable?
    trials = 10000
    solvable = 0
    for _ in range(trials):
        numbers = list(range(9))
        random.shuffle(numbers)
        if is_solvable(tuple(numbers)):
            solvable += 1
    print("Share of solvable random puzzles:", solvable / trials)
