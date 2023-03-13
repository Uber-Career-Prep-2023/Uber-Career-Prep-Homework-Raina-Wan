"""
Raina Wan
03-13-2023

Two Sum:
Given an array of integers and a target integer, k, return the number of pairs of integers in the array that 
sum to k. In each pair, the two items must be distinct elements (come from different indices in the array).

Time Complexity: O(n) => Iterating through array once to get occurrence of repeated values.
Space Complexity: O(n) => Creating dictionary to identify remainder

Technique: Hash The Running Computation

Time Spent:
50 minutes

Approach:
1) Create dictionary where key is the difference between k and the array element
2) If the element equates to a key, a sum has been found. Increment count by one
3) If remainder is not yet in dictionary, set its occurrence to 1. Otherwise, add 1

* See example below *
"""


def TwoSum(arr, k):
    if len(arr) < 2 or not arr: return None

    diff = {} # remainder : occurrence
    count = 0
    
    for i in range(len(arr)):
        remainder = k - arr[i]
        if arr[i] in diff:
            count += diff[arr[i]]
        if remainder in diff:
            diff[remainder] += 1
        else:
            diff[remainder] = 1
    
    return count



def main():
   print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10)) # Output: 3 (Pairs: (8, 2), (8, 2), (3, 7))
   print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 9)) # Output: 4 (Pairs: (10, -1), (1, 8), (2, 7), (2, 7))
   print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6],6)) # Output: 5 (Pairs: (4, 2), (0, 6), (3, 3), (3, 3), (3, 3))
   print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6],1)) # Output: 0

main()

"""
input: arr = [4, 3, 3, 5, 7, 0, 2, 3]
       k = 6
output: pairs = (4, 2), (0, 6), (3, 3), (3, 3), (3, 3)

remainder : occurrence
   2      :     1           count = 0
   3      :     1           count = 0
   3      :     2           count = 1 (element 3 is already in dictionary. add its val, 1)
   5      :     1           count = 1
   7      :     1           count = 1
   0      :     1           count = 1
   4      :     1           count = 2 (element 2 is already in dictionary. add its val, 1)
   3      :     3           count = 5 (element 3 is already in dictionary. add its val, 2)
"""
