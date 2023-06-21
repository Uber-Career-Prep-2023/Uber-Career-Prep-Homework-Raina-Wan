"""
Raina Wan
06-16-2023

Build a Heap:
Write a min heap class according to the following API using an array as the underlying data structure. 
(A max heap has the same implementation; you simply need to flip the direction of the comparators.) For 
simplicity, you can assume that the heap holds integers rather than generic comparables.

Time Spent:
45 minutes
"""
class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        return self.arr[0]

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_index(self, index):
        return 2 * index + 1

    def get_right_index(self, index):
        return 2 * index + 2

    def has_left(self, index):
        return self.get_left_index(index) < len(self.arr)

    def has_right(self, index):
        return self.get_right_index(index) < len(self.arr)

    def swap(self, left, right):
        self.arr[left], self.arr[right] = self.arr[right], self.arr[left]

    def insert(self, val):
        self.arr.append(val)
        self.heapifyUp(len(self.arr) - 1)

    def heapifyUp(self, index):
        if index != 0: # root node
            parent = self.get_parent_index(index)
            child = index

            # keep swapping until child is less than parent
            if (self.arr[parent] > self.arr[child]):
                self.swap(parent, index)
                self.heapifyUp(parent)

    def remove(self):
        if len(self.arr) == 0:
            return -1
        else:
            root = self.arr[0] # current min value
            self.arr[-1], self.arr[0] = self.arr[0], self.arr[-1] # swap root and last node
            self.arr.pop(len(self.arr) - 1) # pop last node (min val)
            if len(self.arr) > 1:
                self.heapifyDown(0)
            return root

    def heapifyDown(self, index):
        left = self.get_left_index(index)
        right = self.get_right_index(index)
        min = index
        
        # if child is greater than root, swap
        if self.has_left(min) and self.arr[left] < self.arr[min]:
            min = left
        if self.has_right(min) and self.arr[right] < self.arr[min]:
            min = right
        if min != index:
            self.swap(min, index)
            self.heapifyDown(min)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(7)
    heap.insert(1)
    heap.insert(9)
    heap.insert(5)
    heap.insert(3)

    print(heap.top())
    # Output: 1

    heap.remove()
    print(heap.top())
    # Output: 3

