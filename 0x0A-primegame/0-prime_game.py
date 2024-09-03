#!/usr/bin/python3
"""
Determine the winner of the Prime Game.
"""


def is_prime_sieve(n):
    """Helper function to create a sieve of prime numbers up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, n + 1, start):
                sieve[multiple] = False
    return sieve


def count_primes_up_to_n(sieve, n):
    """Count the number of primes up to n using a sieve."""
    return sum(sieve[:n + 1])


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if x <= 0 or not nums:
        return None
    max_n = max(nums)
    sieve = is_prime_sieve(max_n)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = count_primes_up_to_n(sieve, n)

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
