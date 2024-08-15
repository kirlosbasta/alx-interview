#!/usr/bin/python3
'''0-rotate_2d_matrix module'''


def rotate_2d_matrix(matrix):
    '''Rotate 2D matrix clockwise in place'''
    N = len(matrix)
    # number of squares in each matrix
    for x in range(int(N / 2)):
        for y in range(x, N - x - 1):
            # save first item in each square
            tmp = matrix[x][y]
            # move left to above
            matrix[x][y] = matrix[N - 1 - y][x]
            # move bottom to left
            matrix[N - 1 - y][x] = matrix[N - 1 - x][N - 1 - y]
            # move right to bottom
            matrix[N - 1 - x][N - 1 - y] = matrix[y][N - 1 - x]
            # move above to right
            matrix[y][N - 1 - x] = tmp
