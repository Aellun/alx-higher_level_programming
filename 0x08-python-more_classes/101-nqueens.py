#!/usr/bin/python3
"""This module Solves the N-Queens puzzle.

Finds all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

N must be an int >=4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

"""
import sys


def init_board(n):
    """Initializes `n`x`n` sized chessboard with with empty spaces's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists rep of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """this function mark areas or spots where quens 
    can mo longer be placed.

    Args:
        board (list): The working chessboard-current.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X'd out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X'd out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X'd out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X'd out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X'd out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X'd out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X'd out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X'd out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """the Recursively function that solve an N-Queens puzzle.

    Args:
        board (list): The working chessboard-current
        row (int): The current-row.
        queens (int):number of placed Queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                    queens + 1, solutions)

            return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
