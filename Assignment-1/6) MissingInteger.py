"""
Raina Wan
03-02-2023

Missing Integer:
Given an integer n and a sorted array of integers of size n-1 which contains
all but one of the integers in the range 1-n, find the missing integer.

Time Complexity: O(n) => iterating through entire array
Space Complexity: O(1) => not storing extra memory

Technique:
Brute force. Can do it in O(logn)?

Time Spent:
15 minutes

Approach:
1) Iterate through array using range based for loop
2) If i doesn't equate to missing integer in array, return that value. Set found to True
3) If haven't found missing integer after full integer, return length of array, n
"""

def MissingInteger(nums, n):
    found = False
    for i in range(n-1):
        if i + 1 != nums[i] and not found:
            ans = i + 1
            found = True
    if not found: 
        ans = n
    return ans

def main():
    print(MissingInteger([1, 2, 3, 4, 6, 7],7)) # Output: 5
    print(MissingInteger([1],2)) # Output: 2
    print(MissingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12],12)) # Output: 9

main()

