#!/usr/bin/python3
"""
N Queens Problem Solver

This script solves the N Queens problem and prints all possible solutions.
The N Queens problem is the challenge of placing N chess queens on an N×N
chessboard so that no two queens threaten each other.
"""
import sys


def solve_queens_problem(board_size):
    """
    Solve the N Queens problem for a given board size.

    Args:
        board_size (int): The size of the chessboard and number of queens.

    Returns:
        list: A list of all valid solutions, where each solution is a list
              representing the positions of queens in each column.
    """

    def is_valid_position(pos, occupied_pos):
        """
        Check if a new queen position is valid given the current occupied
        positions.

        Args:
            pos (int): The row position to check for the current column.
            occupied_pos (list): List of row positions for queens in previous
            columns.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        for i in range(len(occupied_pos)):
            if (
                occupied_pos[i] == pos or
                occupied_pos[i] - i == pos - len(occupied_pos) or
                occupied_pos[i] + i == pos + len(occupied_pos)
            ):
                return False
        return True

    def place_queens(board_size, index, occupied_pos, solutions):
        """
        Recursively place queens on the board to find all valid solutions.

        Args:
            board_size (int): The size of the chessboard.
            index (int): The current column being processed.
            occupied_pos (list): Current partial solution (queen positions).
            solutions (list): List to store all valid solutions.
        """
        if index == board_size:
            solutions.append(occupied_pos[:])
            return

        for i in range(board_size):
            if is_valid_position(i, occupied_pos):
                occupied_pos.append(i)
                place_queens(board_size, index + 1, occupied_pos, solutions)
                occupied_pos.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """
    Main function to handle command-line arguments and print solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()
