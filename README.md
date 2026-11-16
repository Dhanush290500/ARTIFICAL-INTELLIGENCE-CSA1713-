# Artificial Intelligence and Prolog Lab Programs

This repository contains small lab programs for Artificial Intelligence and Prolog. Each program is stored as a separate file in the repository root, alongside a text file with its sample output when available.

## Programs currently in the repository

| File | Topic | Language |
| --- | --- | --- |
| `LAB EXPERIMENT (1)` | 8-puzzle solver | Python |
| `LAB EXPERIMENT (2)` | N-Queens using backtracking | Python |
| `LAB EXPERIMENTS (3)` | Water jug problem | Python |
| `LAB EXPERIMENT (4)` | SEND + MORE = MONEY cryptarithmetic | Python |
| `LAB EXPERIMENTS (5)` | Missionaries and cannibals | Python |
| `LAB EXPERIMENTS (6)` | Vacuum cleaner agent | Python |
| `LAB EXPERIMENTS (7)` | Breadth-first search | Python |
| `LAB EXPERIMENTS (8)` | Depth-first search | Python |
| `LAB EXPERIMENTS (9)` | Travelling salesperson brute-force search | Python |
| `LAB EXPERIMENTS (10)` | A* path search | Python |
| `LAB EXPERIMENTS (11)` | Map coloring with backtracking | Python |
| `LAB EXPERIMENTS (12)` | Tic-tac-toe | Python |

The corresponding `OUTPUT` files show example results. The 8-puzzle source refers to helper functions (`print_board` and `solve_8_puzzle`) that are not defined in that file, so it needs those functions added before it runs as a standalone program. The tic-tac-toe sample output is a captured interactive prompt rather than a completed game.

## Running the Python programs

Install Python 3, then run a program from a terminal. The filenames contain spaces and parentheses, so quote the path:

```sh
python3 'LAB EXPERIMENTS (7)'
```

Some programs wait for keyboard input. In particular, the 8-puzzle and tic-tac-toe programs are interactive. The 8-puzzle program currently needs its missing helper functions before it can run.

## Additional lab topics to add

The following topics were requested as part of the lab work but are not present in the current repository snapshot:

### Python

- Decision tree
- Feed-forward neural network

### Prolog

- Sum integers from 1 to *n*
- Database of names and dates of birth
- Student, teacher, and subject-code database
- Planets database
- Towers of Hanoi
- Bird flight facts and queries
- Family tree
- Diet suggestions based on disease
- Monkey and banana problem
- Fruit colors using backtracking
- Best-first search
- Medical diagnosis
- Forward chaining
- Backward chaining

These should be added as separate, clearly named source files, with sample queries or output alongside each one. Prolog source files should use the `.pl` extension.

## Suggested organization

As the collection grows, group files by language and keep source separate from captured output:

```text
python/
  eight_puzzle.py
  n_queens.py
  ...
prolog/
  sum_1_to_n.pl
  family_tree.pl
  ...
outputs/
  ...
```

This organization is a suggested next step; existing filenames have been kept as-is so current links and lab references continue to work.
