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

## Design decisions

* Plain functions and tuples are used instead of classes. A state is just 9 numbers,
  and tuples can be stored directly in sets and dictionaries (visited states, costs).
  This keeps the code short and fast.
* The heuristic is passed to the A* function as a parameter, so both heuristics
  run through exactly the same search code and the comparison is fair.

## Heuristics

* **Hamming:** number of tiles (without the empty field) that are not on their goal position.
* **Manhattan:** sum of the horizontal and vertical distances of every tile to its goal position.

Both are admissible (they never overestimate the real number of moves), so A* always
finds a shortest solution with either of them.

## Expected output of the tests

* `state.py`: 4 successors of the start state, 2 successors of the goal,
  16 inversions (solvable), 1 inversion for "1 and 2 swapped" (not solvable),
  share of solvable random puzzles about 0.5
* `heuristics.py`: `hamming = 8, manhattan = 18` for the slide start state
* `astar.py`: 26 moves with both heuristics; Hamming expands 44988 nodes, Manhattan 3977

## Results (100 random solvable puzzles, seed 42)

Values calculated from `results.csv` in this repository.

| Heuristic | Nodes mean | Nodes std | Nodes variance | Time mean | Time std | Time variance | Moves (mean) |
|---|---|---|---|---|---|---|---|
| Hamming | 18207.1 | 17047.2 | 290607840 | 0.0511 s | 0.0485 s | 0.002348 s² | 22.4 |
| Manhattan | 1722.0 | 1733.4 | 3004680 | 0.0059 s | 0.0060 s | 0.0000365 s² | 22.4 |

Manhattan expands about 10.6 times fewer nodes than Hamming and is about 8.7 times faster.
Both heuristics found solutions of the same length for all 100 puzzles.

The variance is the square of the standard deviation (calculated from the unrounded
values, so squaring the rounded std in the table gives a slightly different number).
Node counts and moves are always the same with the same seed. Run times depend on the computer.
