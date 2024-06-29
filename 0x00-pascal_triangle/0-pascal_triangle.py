#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    '''Returns a list of lists of integers representing
    the Pascal’s triangle of n'''
    if n <= 0:
        return []
    trinagle = [[1]]
    for i in range(1, n):
        row = []
        row.append(1)
        for j in range(1, i):
            num = trinagle[i - 1][j - 1] + trinagle[i - 1][j]
            row.append(num)
        row.append(1)
        trinagle.append(row)
    return trinagle
