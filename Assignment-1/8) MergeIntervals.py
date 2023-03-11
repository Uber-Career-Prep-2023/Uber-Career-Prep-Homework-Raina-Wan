"""
Raina Wan
03-10-2023

Merge Intervals:
Given a list of integer pairs representing the low and high end of an interval, 
inclusive, return a list in which overlapping intervals are merged.

Time Complexity: O(nlogn) => n for size of intervals; logn for sorting intervals
Space Complexity: O(n) => size of result has a max length of number of intervals

Technique: 
Sort, then solve

Time Spent:
30 minutes

Approach:
1) Sort intervals by first value in tuple
2) Store first interval in result
3) Iterate through sorted intervals and get the previous interval.
    - If the current start value is less than or equal to the previous end value, intervals overlap. Merge.
    - Otherwise, intervals don't overlap. Append interval to result.
4) Return tuple (not list) of intervals
"""

def MergeIntervals(input):
    if not input: return
    
    # sort by first value
    input.sort(key = lambda a : a[0])

    # add first interval to avoid edge case
    res = [list(input[0])]

    for first, last in input[1:]:
        # get end value previous interval
        prev = res[-1][1]
    
        if first <= prev:
            res[-1][1] = max(last, prev) # merge interlapping intervals
        else:
            res.append([first, last])
    
    # convert list back to tuple
    for i in range(len(res)):
        res[i] = tuple(res[i])

    return res
    

def main():
    print(MergeIntervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)])) # Output: [(1, 3), (4, 8), (9, 12)]
    print(MergeIntervals([(5, 8), (6, 10), (2, 4), (3, 6)])) # Output: [(2, 10)]
    print(MergeIntervals([(10, 12), (5, 6), (7, 9), (1, 3)])) # Output: [(1, 3), (5, 6), (7, 9), (10, 12)]


main()
