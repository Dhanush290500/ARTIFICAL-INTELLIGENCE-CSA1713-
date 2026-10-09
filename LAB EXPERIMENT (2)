def solve_n_queens(n):
    solutions = []
    
    # 'board' stores the column index of the queen for each row
    def backtrack(row, board):
        # Base case: If all queens are placed, save the solution
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            # Check if placing a queen at (row, col) is safe
            safe = True
            for i in range(row):
                # We check two things against previously placed queens (at row 'i'):
                # 1. Are they in the same column? (board[i] == col)
                # 2. Are they on the same diagonal? (abs(board[i] - col) == abs(i - row))
                if board[i] == col or abs(board[i] - col) == abs(i - row):
                    safe = False
                    break
            
            # If safe, place the queen and move to the next row
            if safe:
                board[row] = col
                backtrack(row + 1, board)
                # No explicit board reset is needed here because the 
                # 'board[row] = col' will just be overwritten in the next iteration.

    # Start backtracking from row 0 with an empty board of size n
    backtrack(0, [-1] * n)
    return solutions

def print_solution(solution):
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)

# Solve for an 8x8 board
n = 8
all_solutions = solve_n_queens(n)

print(f"Total valid arrangements found: {len(all_solutions)}\n")
print("Visualizing the first solution:")
print_solution(all_solutions[0])
