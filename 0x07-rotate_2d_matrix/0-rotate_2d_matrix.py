#!/usr/bin/python3
"""
Module to rotate a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    
    Args:
    matrix (list of list of int): The n x n 2D matrix to rotate.
    """
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
