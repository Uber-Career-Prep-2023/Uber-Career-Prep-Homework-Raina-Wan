"""
Raina Wan
04-09-2023

Doubly Linked List
"""

class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates new Node with data at front; new head
    def push_front(self, value):
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = None
        return self.head.val
    
    # creates new Node with data val at end
    def push_back(self, value):
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next # find last element of list
            new_node = Node(value)
            curr.next = new_node
            new_node.prev = curr
            new_node.next = None

    # creates new Node with data val after Node loc
    def push_node(self, val, i):
        if i == self.length() or not self.head or i < 0:
            return
        elif i == (self.length() - 1):
            self.push_back(val)
        else:
            curr = self.head
            count = 0
            while count != i:
                curr = curr.next
                count += 1
            new_node = Node(val)
            new_node.next = curr.next
            new_node.prev = curr
            curr.next.prev = new_node
            curr.next = new_node
            
    
    # removes first Node; returns new head
    def pop_front(self):
        if self.head:
            dummy = Node(0)
            dummy.next = self.head.next
            self.head = dummy.next
            self.prev = None
        return self.head.val
    
    # removes last Node
    def pop_back(self):
        if self.head:
            curr = self.head
            prev = self.head
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
    
    # removes node at index; returns head
    def pop_node(self, i):
        if i == self.length():
            return
        elif i == 0: 
            self.pop_front()
        elif i == self.length() - 1:
            self.pop_back()
        else:
            prev, curr = self.head, self.head
            count = 0
            while count != i:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = curr.next
            curr.next.prev = prev
        return self.head.val
    
    # returns length of linked list
    def length(self):
        if not self.head:
            return 0
        curr = self.head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        return count

    # reverses Linked List iteratively
    def reverseIterative(self, head):
        if not self.head:
            return
        temp = None
        curr = self.head
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev
    
    # reverses Linked List recursively
    def reverseRecursive(self, head):
        if not self.head:
            return None
        # swap head's next and prev
        temp = self.head.prev
        self.head.prev = self.head.next
        self.head.next = temp

        if not self.head.prev:
            return self.head
        else:
            self.reverseRecursive(self.head.prev)
        
    # prints list
    def print(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        print('| ', end="")
        for i in res: 
            print(i, end = " | ")

def main():
    list = DoublyLinkedList()

    list.push_front(2)          # | 2 |
    list.push_front(5)          # | 5 | 2 |
    list.push_front(6)          # | 6 | 5 | 2 |
    list.push_back(7)           # | 6 | 5 | 2 | 7 |
    list.push_back(8)           # | 6 | 5 | 2 | 7 | 8 |
    list.push_back(9)           # | 6 | 5 | 2 | 7 | 8 | 9 |
    list.push_node(1,4)         # | 6 | 5 | 2 | 7 | 8 | 1 | 9 |
    list.reverseIterative(6)    # | 9 | 1 | 8 | 7 | 2 | 5 | 6 |
    list.pop_front()            # | 1 | 8 | 7 | 2 | 5 | 6 |
    list.pop_back()             # | 1 | 8 | 7 | 2 | 5 |
    list.pop_node(2)            # | 1 | 8 | 2 | 5 |
    
    list.print()

main()

