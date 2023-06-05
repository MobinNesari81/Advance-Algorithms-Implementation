def solve_n_queens(n):
    """
    Solves the n-queens problem for a board of size n.
    Returns a list of solutions, where each solution is a list
    of column indices corresponding to the queen positions on
    each row.
    """
    # Initialize an empty board.
    board = [-1] * n
    
    # Initialize variables to keep track of solutions.
    solutions = []
    num_solutions = 0
    
    # Define a helper function to check if a given queen placement is valid.
    def is_valid(row, col):
        # Check if there is a queen in the same column.
        if col in board:
            return False
        
        # Check if there is a queen on the same diagonal (upper left to lower right).
        if any(row - i == abs(col - j) for i, j in enumerate(board[:row])):
            return False
        
        # Check if there is a queen on the same diagonal (lower left to upper right).
        if any(row + i == abs(col - j) + (n - 1) for i, j in enumerate(board[:row])):
            return False
        
        # If all checks pass, the placement is valid.
        return True
    
    # Define a recursive function to place queens on the board.
    def place_queen(row):
        nonlocal num_solutions
        
        # Base case: all rows are filled.
        if row == n:
            solutions.append(list(board))
            num_solutions += 1
            return
        
        # Try placing a queen in each column of the current row.
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                place_queen(row + 1)
                board[row] = -1  # backtrack
    
    # Start recursive function with the first row.
    place_queen(0)
    
    # Return list of solutions.
    return solutions
