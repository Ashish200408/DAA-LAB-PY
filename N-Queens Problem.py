# N-Queens Problem using Backtracking

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # If all queens are placed
    if row == n:
        return True

    # Try placing queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = 0  # Backtrack

    return False


# Input
n = int(input("Enter number of queens: "))

# Initialize board
board = [[0 for _ in range(n)] for _ in range(n)]

# Solve
if solve_n_queens(board, 0, n):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists")