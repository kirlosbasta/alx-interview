#!/usr/bin/python3
'''
0-island_perimeter
'''

def island_perimeter(grid):
    '''return the perimeter of the island'''
    height, width, res = len(grid), len(grid[0]), 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                sides = 4
                if j + 1 < width and grid[i][j + 1] == 1:
                    sides -= 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    sides -= 1
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    sides -= 1
                if i + 1 < height and grid[i + 1][j] == 1:
                    sides -= 1
                res += sides
    return res
