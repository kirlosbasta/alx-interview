#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    '''Returns a list of lists of integers representing
    the Pascal’s triangle of n'''
    if n <= 0:
        return []
    # the first row is always the same 1
    trinagle = [[1]]
    for i in range(1, n):
        row = []
        # add the first number 1
        row.append(1)
        for j in range(1, i):
            # the num is the sum of the above two numbers
            num = trinagle[i - 1][j - 1] + trinagle[i - 1][j]
            row.append(num)
        # add the last number 1
        row.append(1)
        trinagle.append(row)
    return trinagle
