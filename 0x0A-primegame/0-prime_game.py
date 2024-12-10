#!/usr/bin/python3

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_up_to(max_n):
    """Generate a list indicating if numbers up to max_n are prime."""
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False
    return primes

def count_primes_up_to(n, primes):
    """Count the number of primes up to n using the precomputed list."""
    return sum(primes[:n + 1])

def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = generate_primes_up_to(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n, primes)

        # If the number of primes is odd, Maria wins; otherwise, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

