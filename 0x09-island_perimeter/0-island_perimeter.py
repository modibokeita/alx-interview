#!/usr/bin/python3
"""
This module defines a function to calculate the perimeter of an island
represented as a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): 2D list representing the grid.
                                    0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                # Add 4 for the current cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                if row > 0 and grid[row - 1][col] == 1:  # Check above
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
