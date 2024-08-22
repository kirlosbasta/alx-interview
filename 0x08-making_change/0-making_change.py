#!/usr/bin/python3
'''0-making_change'''


def makeChange(coins: list, total: int):
    '''return the least amount of coin to make total'''
    sorted_coins = sorted(coins, reverse=True)
    if total <= 0:
        return 0
    count = 0
    for i in range(len(sorted_coins)):
        while total >= sorted_coins[i]:
            count += 1
            total -= sorted_coins[i]
    return count if total == 0 else -1
