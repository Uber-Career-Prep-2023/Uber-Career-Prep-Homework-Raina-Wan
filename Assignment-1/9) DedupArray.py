"""
Raina Wan
03-11-2023

Dedup Array:
Given a sorted array of non-negative integers, modify the array by removing duplicates so each element 
only appears once. If arrays are static (aka, not dynamic/resizable) in your language of choice, the 
remaining elements should appear in the left-hand side of the array and the extra space in the right-hand 
side should be padded with -1s.

Time Complexity: O(n) => Iterating through input array one time
Space Complexity: O(1) => Modifying array in place by removing elements

Technique:
Array Iteration

Time Spent:
20 minutes

Approach:
1) Store first value of array in previous variable
2) Iterate through array using while loop (not for loop because updating the range)
3) If the current value is equal to the previous value, remove from array. Decrease i and length values by 1
4) Otherwise, set previous variable to current value
5) Update i counter
"""

def DedupArray(arr):
    if not arr: return arr

    prev = arr[0]
    i = 1
    length = len(arr)

    while i < length:
        if arr[i] == prev:
            del arr[i]
            i -= 1
            length -= 1
        else:
            prev = arr[i]
        i += 1

    return arr

def main():
    print(DedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])) # Output: [1, 2, 3, 4]
    print(DedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15])) # Output: [0, 1, 4, 5, 8, 9, 10, 11, 15]
    print(DedupArray([1, 3, 4, 8, 10, 12])) # Output: [1, 3, 4, 8, 10, 12]

main()
