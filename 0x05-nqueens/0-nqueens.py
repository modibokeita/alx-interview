#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """ Check if it's safe to place a queen at board[row][col] """
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check the upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row, N, solutions):
    """ Solves the N queens problem using backtracking """
    if row == N:
        # All queens are placed, add the solution to solutions
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    
    # Try placing the queen in all columns
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place the queen
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0  # Backtrack

def main():
    # Check if we have the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Try to convert the input to an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with 0s
    board = [[0 for _ in range(N)] for _ in range(N)]

    # List to store all solutions
    solutions = []

    # Start solving from the first row
    solve_nqueens(board, 0, N, solutions)

    # Print each solution
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

