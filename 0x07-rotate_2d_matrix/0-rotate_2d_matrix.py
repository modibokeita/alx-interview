#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.
    """
    n = len(matrix)
    # Perform a layer-by-layer rotation
    for layer in range(n // 2):
        start = layer
        end = n - layer - 1
        for i in range(start, end):
            # Save the top element
            top = matrix[start][i]
            # Move left element to top
            matrix[start][i] = matrix[n - i - 1][start]
            # Move bottom element to left
            matrix[n - i - 1][start] = matrix[end][n - i - 1]
            # Move right element to bottom
            matrix[end][n - i - 1] = matrix[i][end]
            # Assign top element to right
            matrix[i][end] = top

