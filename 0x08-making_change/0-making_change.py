#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to meet the given total.
    
    Parameters:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target amount to achieve with the fewest coins.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        count = total // coin  # Use as many of this coin as possible
        num_coins += count
        total -= count * coin  # Reduce the remaining total

    return num_coins if total == 0 else -1

