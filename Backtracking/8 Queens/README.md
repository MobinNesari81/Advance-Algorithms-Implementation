# 8 Queens Problem with Backtracking

To use this function for the 8 queens problem, simply call `solve_n_queens(8)` and it will return a list of all solutions for an 8x8 chessboard. Each solution is represented as a list of column indices corresponding to the queen positions on each row.

Example usage:

```python
solutions = solve_n_queens(8)
print("Number of solutions:", len(solutions))
for i, solution in enumerate(solutions):
    print("Solution", i + 1, ":", solution)
```

This will output:

```
Number of solutions: 92
Solution 1 : [0, 4, 7, 5, 2, 6, 1, 3]
Solution 2 : [0, 5, 7, 2, 6, 3, 1, 4]
Solution 3 : [0, 6, 3, 5, 7, 1, 4, 2]
Solution 4 : [0, 6, 4, 7, 1, 3, 5, 2]
Solution 5 : [1, 3, 5, 7, 2, 0, 6, 4]
...
```

Each solution represents a valid placement of 8 queens on an 8x8 chessboard such that no two queens threaten each other (i.e., no two queens share the same row, column, or diagonal).