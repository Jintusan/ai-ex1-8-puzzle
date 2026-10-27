# 8-Puzzle with A* Search

Exercise 1 - Introduction to Artificial Intelligence & Data Science (FH Campus Wien).

Solves the 8-puzzle with A* and compares two heuristics (Hamming and Manhattan)
on 100 random solvable start states.

## Files

| File | Job |
|---|---|
| `state.py` | represent the puzzle, generate moves, random start states, solvability check |
| `heuristics.py` | the two heuristics (misplaced tiles = Hamming, Manhattan distance) |
| `astar.py` | the A* search (heuristic is passed as a parameter) |
| `experiment.py` | solve 100 puzzles with both heuristics, measure, print table, save `results.csv` |
| `results.csv` | all 200 single measurements (output of `experiment.py`) |

Only Python 3 is needed (standard library only).

## How to run

Every file can be started on its own and has a small test at the bottom:

```bash
python state.py          # successors, solvability checks
python heuristics.py     # hamming/manhattan values (start state: 8 and 18)
python astar.py          # solves the slide example with both heuristics (26 moves)
python experiment.py     # the full experiment, takes about 1-3 minutes
```
(On Mac/Linux you may need `python3` instead of `python`.)

## Representation

* A state is a tuple of 9 numbers, read row by row, `0` = empty field.
* Goal state: `(0, 1, 2, 3, 4, 5, 6, 7, 8)` (empty field top left, as on the exercise slide).
* Start state from the slides: `(7, 2, 4, 5, 0, 6, 8, 3, 1)`.

## Expected output of the tests

* `state.py`: 4 successors of the start state, 2 successors of the goal,
  16 inversions (solvable), 1 inversion for "1 and 2 swapped" (not solvable),
  share of solvable random puzzles about 0.5
* `heuristics.py`: `hamming = 8, manhattan = 18` for the slide start state
* `astar.py`: 26 moves with both heuristics; Hamming expands 44988 nodes, Manhattan 3977

## Results (100 random solvable puzzles, seed 42)

| Heuristic | Nodes mean | Nodes std | Time mean | Time std | Moves |
|---|---|---|---|---|---|
| Hamming | 18207.1 | 17047.2 | 0.1209 s | 0.1283 s | 22.4 |
| Manhattan | 1722.0 | 1733.4 | 0.0136 s | 0.0155 s | 22.4 |

Node counts and moves are always the same with the same seed. Run times depend on the computer.
