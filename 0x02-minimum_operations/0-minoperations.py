#!/usr/bin/python3
'''0. Minimum Operations'''


def minOperations(n):
    '''return the minimum amount of operation needed to reach n'''
    def prime_factors(n):
        '''return al list of prime numbers of n'''
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    if n <= 1:
        return 0
    factors = prime_factors(n)
    return sum(factors)
