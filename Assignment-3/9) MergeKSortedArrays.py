"""
Raina Wan
06-21-2023

Merge K Sorted Arrays:
Given an array of k sorted arrays, merge the k arrays into a single sorted array.

Time Complexity: O(k logn) => insertion operation for heap is O(log n). There are k arrays
Space Complexity: O(k) => heap contains k arrays

Technique:
Heap

Time Spent:
25 minutes

Approach:
1) Push all elements from arrays into one list
2) Pop the minimum element using heappop and add to res
"""

import heapq

def merge_k_arrays(k, arrays):
    curr, res = [], []
    for array in arrays:
        for i in array:
            heapq.heappush(curr, i) # push all numbers to curr
    
    while curr:
        min = heapq.heappop(curr) # pop smallest val and add to res
        res.append(min)
    
    return res

if __name__ == "__main__":
    print(merge_k_arrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
    # Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

    print(merge_k_arrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
    # Output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
