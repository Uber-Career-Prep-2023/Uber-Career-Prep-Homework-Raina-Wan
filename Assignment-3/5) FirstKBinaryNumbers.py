"""
Raina Wan
06-05-2023

First K Binary Numbers:
Given a number, k, return an array of the first k binary numbers, represented as strings.

Time Complexity: O(k) => queue appends values k number of times
Space Complexity: O(k) => adding k string elements to result

Technique:
Breadth-first search

Time Spent:
40 minutes (could not figure out DFS solution)

Approach:
1) Create a queue of values, adding 0 and 1 (in that order) for each iteration.
2) As long as the result has not reached a length of k, pop the leftmost value and append it to res.
"""

from collections import deque

def first_k_binary(k):
    if k <= 0: return []

    res = ['0']
    q = deque()
    q.append('1')

    while len(res) < k:
        num = q.popleft()
        if num:
            res.append(num)
        q.append(num + '0')
        q.append(num + '1')

    return res

def main():
    print(first_k_binary(5))    # Output: ['0', '1', '10', '11', '100']
    print(first_k_binary(10))   # Output: ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']

main()
