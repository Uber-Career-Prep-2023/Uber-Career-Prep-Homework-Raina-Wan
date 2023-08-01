"""
Raina Wan
07-21-2023

Catalan Numbers:
The Catalan numbers are a mathematical sequence of numbers. The nth Catalan 
number is defined as (2n)! / (n+1)!n!. Given a non-negative integer n, return 
the Catalan numbers 0-n.

Time Complexity: O(n) => get catalan of every number up to n
Space Complexity: O(n) => storing n values in result

Time Spent:
20 minutes
"""


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def catalan_numbers(n):
    res = []
    for i in range(n+1):
        top = factorial(2 * i)
        bottom = factorial(i + 1) * factorial(i)
        res.append(top // bottom)
    return res

if __name__ == "__main__":
    print(catalan_numbers(1))
    # Output: [1, 1]

    print(catalan_numbers(5))
    # Output: [1, 1, 2, 5, 14, 42]