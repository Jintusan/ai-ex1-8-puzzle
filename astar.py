# ============================================================
# astar.py
# A* search for the 8-puzzle.
# The heuristic is passed as a parameter, so the same search
# can be used with different heuristics.
# ============================================================

import heapq
from state import GOAL, successors


def reconstruct_path(parent, state):
    """
    Input:    parent - dictionary {state: previous state}
              state  - the goal state that was reached
    Output:   list of states from the start state to the goal state
    Function: Follows the parent links backwards from the goal to the start
              and then reverses the list.
    """
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    path.reverse()
    return path


def astar(start, heuristic):
    """
    Input:    start     - start state (tuple of 9 numbers), must be solvable
              heuristic - function that estimates the remaining moves for a state
    Output:   (path, expanded)
              path     - list of states from start to goal (None if no solution)
              expanded - number of expanded nodes (measure for memory effort)
    Function: Always expands the state with the lowest f = g + h, where
              g = moves made so far and h = estimated moves still needed.
    """
    counter = 0                     # tie-breaker: if f is equal, the older entry comes first
    frontier = [(heuristic(start), counter, start)]   # waiting list: (f, counter, state)
    g = {start: 0}                  # cheapest known number of moves to each state
    parent = {start: None}          # where each state was reached from
    visited = set()                 # states that are already expanded
    expanded = 0

    while frontier:
        f, _, state = heapq.heappop(frontier)    # state with the lowest f

        if state in visited:        # already expanded via a shorter way -> skip
            continue

        if state == GOAL:           # goal reached
            return reconstruct_path(parent, state), expanded

        visited.add(state)          # expand this state
        expanded += 1

        for nxt in successors(state):
            new_g = g[state] + 1    # every move costs 1
            if nxt not in g or new_g < g[nxt]:   # new or shorter way found
                g[nxt] = new_g
                parent[nxt] = state
                counter += 1
                heapq.heappush(frontier, (new_g + heuristic(nxt), counter, nxt))

    return None, expanded           # frontier empty -> no solution


# ------------------------------------------------------------
# Tests: only run when this file is started directly
# ------------------------------------------------------------
if __name__ == "__main__":
    from state import show
    from heuristics import hamming, manhattan

    start = (7, 2, 4, 5, 0, 6, 8, 3, 1)

    for name, h in [("Hamming", hamming), ("Manhattan", manhattan)]:
        path, expanded = astar(start, h)
        print(name, "-> moves:", len(path) - 1, ", expanded nodes:", expanded)

    print("\nSolution (Manhattan), first 3 steps:")
    path, _ = astar(start, manhattan)
    for s in path[:3]:
        show(s)
