#!/usr/bin/python3
'''
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard
'''


import sys


def is_safe(b, r, c, N):

    '''check whether is safe to place a queen in a position'''
    for i in range(r):
        if b[i][c] == 1:
            return False

    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if b[i][j] == 1:
            return False

    for i, j in zip(range(r, -1, -1), range(c, N)):
        if b[i][j] == 1:
            return False

    return True


def explore_nqueens(b, r, N):
    '''explore the puzzle'''
    if r == N:
        print([[i, b[i].index(1)] for i in range(N)])
        return

    for c in range(N):
        if is_safe(b, r, c, N):
            b[r][c] = 1
            explore_nqueens(b, r + 1, N)
            b[r][c] = 0


def nqueens(N):
    '''solve the puzzle'''
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    b = [[0 for _ in range(N)] for _ in range(N)]
    explore_nqueens(b, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
