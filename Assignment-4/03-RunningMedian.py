"""
Raina Wan
07-14-2023

Running Median:
You will be given a stream of numbers, one by one. After each new number, return the 
median of the numbers so far. If the list is even, return the mean of the two middle values.

Time Complexity: Pushing to heap O(log n); Popping from heap O(1)
Space Complexity: O(n) => n is number of elements pushed to heap

Time Spent:
35 minutes
"""

import heapq
class FindMedian:

    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num):
        # python only has min heap. push -num to small heap for a MaxHeap
        heapq.heappush(self.small, -1 * num)

        # make sure every num in small <= num in large.
        # pop largest val in small (maxheap) and compare to smallest val in large (minheap)
        if (self.small and self.large and 
        (-1 * self.small[0]) > self.large[0]): # popping from heap is O(1)
            curr = -1 * heapq.heappop(self.small) # since we added -num, must get back the positive num
            heapq.heappush(self.large, curr)

        # size of two heaps must be equal or difference of 1

        # if small is size 3 and large is size 1, pop from small and push to large
        if len(self.small) > len(self.large) + 1:
            curr = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large, curr)

        if len(self.large) > len(self.small) + 1:
            curr = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * curr)

    def running_median(self):
        # odd length
        # if small > large, return greatest value in small
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        # if large > small, return smallest value in large
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        # even length
        # take sum of (max of small + min of large) / 2
        else:
            lower_mid = -1 * self.small[0]
            higher_mid = self.large[0]
            return (lower_mid + higher_mid) / 2

if __name__ == "__main__":
    median = FindMedian()

    median.add_num(1)
    print(median.running_median())
    # Output: 1

    median.add_num(11)
    print(median.running_median())
    # Output: 6

    median.add_num(4)
    print(median.running_median())
    # Output: 4

    median.add_num(15)
    print(median.running_median())
    # Output: 7.5

    median.add_num(12)
    print(median.running_median())
    # Output: 11