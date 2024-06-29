#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    '''Returns a list of lists of integers representing
    the Pascal’s triangle of n'''
    if n <= 0:
        return []
    trinagle = []
    for i in range(n):
        if i == 0:
            trinagle.append([1])
            continue
        elif i == 1:
            trinagle.append([1, 1])
            continue
        row = []
        for j in range(i):
            if j == 0:
                row.append(1)
                continue
            num = trinagle[i - 1][j - 1] + trinagle[i - 1][j]
            row.append(num)
            if j == i - 1:
                row.append(1)
        trinagle.append(row)
    return trinagle
