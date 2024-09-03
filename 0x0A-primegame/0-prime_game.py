#!/usr/bin/python3
"""
Determine the winner of the Prime Game.
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    """
    def sieve_of_eratosthenes(n):
        """Generate all prime numbers up to n using Sieve of Eratosthenes."""
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]
    def play_round(n):
        """Simulate a round of the game and return the winner."""
        primes = sieve_of_eratosthenes(n)
        maria_moves = ben_moves = 0
        while primes:
            prime = primes.pop(0)
            maria_moves += 1
            primes = [p for p in primes if p % prime != 0]
            if not primes:
                break
            prime = primes.pop(0)
            ben_moves += 1
            primes = [p for p in primes if p % prime != 0]
        return 'Maria' if maria_moves > ben_moves else 'Ben'
    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_round(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
