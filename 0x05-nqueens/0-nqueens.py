#!/usr/bin/python3
'''0-nqueens.py'''
import sys


if len(sys.argv) > 2 or len(sys.argv) <= 1:
    print('Usage: nqueens N')
    exit(1)

n = int(sys.argv[1]) if sys.argv[1].isdigit() else None

if type(n) != int:
    print('N must be a number')
    exit(1)
elif n < 4:
    print('N must be at least 4')
    exit(1)


def is_safe(board, row, col):
    '''check if cell at row, col is safe'''
    # check each cel in the row 
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    # check each cell on upper left diagonal
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
        
    i, j = row, col
    # check each cell on lower left diagonal
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_board_util(board, col):
    '''check all possible solution using recursive backtracking'''
    # Base case to check if the problem is already is solved
    if col >= n:
        result = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    result.append([i, j])
        solution.append(result)
        return True
    res = False
    # check each row in col to match a queen
    for row in range(n):
        if is_safe(board, row, col):
            # initiate a queen
            board[row][col] = 1

            # call the next col
            res = solve_board_util(board, col + 1) or res

            # backtrack if can't go further
            board[row][col] = 0

    return res



def solve_board(n):
    '''sovle N queen problem'''
    board = [ [ 0 for j in range(n) ] for i in range(n) ]
    solve_board_util(board, 0)

    solution.sort()    
    for row in solution:
        print(row)


if __name__ == '__main__':
    solution = []
    solve_board(n)
