"""
Raina Wan
07-21-2023

Coin change:
Given a list of coin denominations and a target sum, return the 
number of possible ways to make change for that sum.

Time Complexity: O(m * n) => m is number of coins and n is amount from 0 to targetSum
Space Complexity: O(m * n) => creating cache with all sum possibilites, using bottom-up dp

Time Spent:
45 minutes
"""


from collections import defaultdict

def coin_change(coins, targetSum):
    cache = {}

    def dfs(index, coin):
        # ex) if nickel == 5, one way to sum
        if coin == targetSum:
            return 1

        # ex) dime > 5 => no way to sum to 5
        if coin > targetSum:
            return 0

        # out of bounds
        if index == len(coins):
            return 0

        if (index, coin) in cache:
            return cache[(index, coin)]
        
        
        # two options: 
        # 1) choose coin at index i. new amount + coin at index i
        # 2) skip coin at index. amt stays same but must increment index
        cache[(index, coin)] = dfs(index, coin + coins[index]) + dfs(index + 1, coin)

        return cache[(index, coin)]
        
    return dfs(0, 0)

if __name__ == "__main__":
    print(coin_change([2, 5, 10], 20))
    # Output: 6
    # Options: ten 2s, four 5s, two 10s, five 2s + two 5s, five 2s + one 10, two 5s + one 10

    print(coin_change([2, 5, 10], 15))
    # Output: 3
    # Options: 10 + 5, three 5s, five 2s + 5