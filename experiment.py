# ============================================================
# experiment.py
# Main program: solves 100 random puzzles with both heuristics,
# measures expanded nodes and run time, and prints statistics.
# ============================================================

import csv
import random
import statistics
import time

from state import random_state
from heuristics import hamming, manhattan
from astar import astar

N_RUNS = 100        # number of random start states
SEED = 42           # fixed seed -> the same 100 puzzles every time

HEURISTICS = [("Hamming", hamming), ("Manhattan", manhattan)]


def run_experiment(n_runs, seed):
    """
    Input:    n_runs - number of random start states
              seed   - seed for the random generator
    Output:   dictionary {heuristic name: {"expanded": [...], "time": [...], "moves": [...]}}
    Function: Creates n_runs random solvable start states and solves each one
              with every heuristic. Measures expanded nodes, run time and
              solution length for every run.
    """
    random.seed(seed)
    starts = [random_state() for _ in range(n_runs)]   # same puzzles for both heuristics

    results = {name: {"expanded": [], "time": [], "moves": []} for name, _ in HEURISTICS}

    for i, start in enumerate(starts, 1):
        for name, h in HEURISTICS:
            t0 = time.perf_counter()
            path, expanded = astar(start, h)
            duration = time.perf_counter() - t0

            results[name]["expanded"].append(expanded)
            results[name]["time"].append(duration)
            results[name]["moves"].append(len(path) - 1)

        print(f"Puzzle {i}/{n_runs} done")   # progress
    return results


def print_table(results):
    """
    Input:    results - dictionary from run_experiment()
    Output:   none (prints a table to the terminal)
    Function: Calculates mean and standard deviation of expanded nodes
              and run time for every heuristic and prints them.
    """
    print("\n{:<10} {:>15} {:>15} {:>12} {:>12} {:>10}".format(
        "Heuristic", "Nodes mean", "Nodes std", "Time mean", "Time std", "Moves"))
    for name, r in results.items():
        print("{:<10} {:>15.1f} {:>15.1f} {:>11.4f}s {:>11.4f}s {:>10.1f}".format(
            name,
            statistics.mean(r["expanded"]), statistics.stdev(r["expanded"]),
            statistics.mean(r["time"]), statistics.stdev(r["time"]),
            statistics.mean(r["moves"])))


def save_csv(results, filename):
    """
    Input:    results  - dictionary from run_experiment()
              filename - name of the CSV file
    Output:   none (writes a file)
    Function: Saves all single measurements to a CSV file, so they can be
              used later for the documentation (e.g. in Excel).
    """
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["run", "heuristic", "expanded", "time_s", "moves"])
        for name, r in results.items():
            for i in range(len(r["expanded"])):
                writer.writerow([i + 1, name, r["expanded"][i], r["time"][i], r["moves"][i]])


if __name__ == "__main__":
    results = run_experiment(N_RUNS, SEED)

    # Check: both heuristics are admissible, so both must find equally short solutions
    same = results["Hamming"]["moves"] == results["Manhattan"]["moves"]
    print("\nBoth heuristics found solutions of the same length:", same)

    print_table(results)
    save_csv(results, "results.csv")
    print("\nAll single results saved to results.csv")
