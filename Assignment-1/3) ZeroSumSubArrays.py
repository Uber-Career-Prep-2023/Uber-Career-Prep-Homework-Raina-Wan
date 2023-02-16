"""
Raina Wan
02-15-2023

Zero Sum Sub Arrays
Given an array of integers, count the number of subarrays that sum to zero.
"""


def ZeroSumSubArrays(nums):
    cur_sum, count = 0, 0
    prev_sums = set([0]) # edge case for when there is a 0 inside nums

    for i in nums:
        cur_sum += i
        if cur_sum in prev_sums:
            count += 1
        else:
            prev_sums.add(cur_sum)

    print(count)
    return count

def main():
    ZeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7]) # result: 2
    ZeroSumSubArrays([1, 8, 7, 3, 11, 9])             # result: 0
    ZeroSumSubArrays([8, -5, 0, -2, 3, -4])           # result: 2

main()



"""
Time Complexity: O(n) => iterating one time where n is the size of the array
Space Complexity: O(n) => n is the size of the set

Technique:
Hash The Running Computation

Time Spent:
40 minutes

Approach:
- iterate through nums
- store the current sum inside a hashmap
- if we revisit a sum in hashmap, then the difference of 
  those nums equate to zero so increment counter

Example:
    nums = [4, 5, 2, -1, -3, -3, 4, 6, -7]
    set =  {4, 9, 11, 10, 7, 4,  8, 14, 7}

    there are two occurrences of 4 and 7. the subarrays that sum to zero are the values between:
    [5, 2, -1, -3, -3] and [-3, 4, 6, -7]
"""
