"""
Raina Wan
06-16-2023

Build a Priority Queue:
A priority queue functions like a queue except that elements are removed in order of priority rather 
than insertion. This is typically implemented as a max heap that stores pairs of elements and numeric 
weights, with the weights used as the values in the heap. Implement a priority queue according to the 
following API using a heap as the underlying data structure. For simplicity, you can assume the priority 
queue stores string elements with integer priorities. Start by copy-pasting your heap implementation from 
question 2 and making modifications.

Time Spent:
20 minutes
"""
class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        return self.arr[0] if self.arr else None

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

    def insert(self, str, weight):
        self.arr.append((str, weight))
        self.heapifyUp(len(self.arr) - 1)

    def heapifyUp(self, index):
        if index != 0: # root node
            parent = self.get_parent_index(index)
            child = index

            # keep swapping until child is less than parent
            if (self.arr[parent][1] > self.arr[child][1]):
                self.swap(parent, index)
                self.heapifyUp(parent)

    def remove(self):
        if len(self.arr) == 0:
            return -1
        else:
            root = self.arr[0] # current min value
            self.swap(0,-1) # swap root and last node
            self.arr.pop(len(self.arr) - 1) # pop last node (min val)
            if len(self.arr) > 1:
                self.heapifyDown(0)
            return root

    def heapifyDown(self, index):
        left = self.get_left_index(index)
        right = self.get_right_index(index)
        min = index
        
        # if child is greater than root, swap
        if self.has_left(min) and self.arr[left][1] < self.arr[min][1]:
            min = left
        if self.has_right(min) and self.arr[right][1] < self.arr[min][1]:
            min = right
        if min != index:
            self.swap(min, index)
            self.heapifyDown(min)


if __name__ == "__main__":
    q = PriorityQueue()
    q.insert("NY", 3)
    q.insert("SF", 2)
    q.insert("CO", 8)
    q.insert("TX", 9)
    q.insert("LA", 4)

    print(q.top())
    # Output: ('SF', 2)

    q.remove()
    print(q.top())
    # # Output: ('NY', 3)

