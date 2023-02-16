"""
Raina Wan
01-30-2023

MaxMeanSubArray:
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

Time Complexity: O(n) for searching through the array once. 'n' is the size of the array
Space Complexity: O(1) space taken by array is fixed, not dynamic

Technique:
Fixed-Size Sliding Window

Time Spent:
35 minutes

Approach:
1) Create two pointers that indicate the length of k
2) Calculate the sum of nums between the range of the two pointers and divide by k
3) Compare previous max mean to current mean and determine which is greater
4) Increment the pointers by one 
5) Return max mean
"""


def max_mean_subarray(nums, k):
    l, r = 0, k
    max_mean = -1
    
    if not nums or len(nums) < k:
        return 

    while r < len(nums) + 1:
        # print(r)
        print(sum(nums[l:r]))
        max_mean = max(max_mean, sum(nums[l:r]) / k)
        l += 1
        r += 1
    return max_mean

def main():
    print(max_mean_subarray([4, 5, -3, 2, 6, 1], 2)) # Output: 4.5
    print(max_mean_subarray([4, 5, -3, 2, 6, 1], 3)) # Output: 3.0
    print(max_mean_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 3)) # Output: 1.333 
    print(max_mean_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 4)) # Output: 1.5


main()

