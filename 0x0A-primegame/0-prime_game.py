#!/usr/bin/python3
"""Prime Game"""

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isWinner(x, nums):
    """Determine the winner of each round"""
    if not nums or x < 1:
        return None
    
    ben_wins = 0
    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            ben_wins += 1

    if ben_wins > x // 2:
        return "Ben"
    elif ben_wins < x // 2:
        return "Maria"
    else:
        return None
