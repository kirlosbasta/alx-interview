#!/usr/bin/python3
'''0-prime_game.py
Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take
turns choosing a prime number from the set and removing
that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
'''


def get_winner(n):
    '''return the winner for each round'''
    prime = [True for i in range(n+1)]
    counter = 0
    p = 2
    while (p <= n):

        if (prime[p] is True):
            for i in range(p, n+1, p):
                prime[i] = False

        while (p <= n and not prime[p]):
            p += 1
        counter += 1

    if counter % 2 == 0:
        return 'Ben'
    else:
        return 'Maria'


def isWinner(x, nums):
    '''return who is the winner for prime_game'''
    players = {'Ben': 0, 'Maria': 0}
    memo = {}

    if not x or len(nums) == 0:
        return None

    n = 0
    for i in range(x):
        if i >= len(nums):
            n = 0

        if memo.get(nums[n]):
            winner = memo.get(nums[n])
        else:
            winner = get_winner(nums[n])
            memo[nums[n]] = winner

        players[winner] += 1
        n += 1

    if players['Ben'] > players['Maria']:
        return 'Ben'
    elif players['Maria'] > players['Ben']:
        return 'Maria'
    else:
        return None
