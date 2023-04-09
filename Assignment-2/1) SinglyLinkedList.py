"""
Raina Wan
04-08-2023

Singly Linked List
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
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
            self.head = new_node
        return self.head.val
    
    # creates new Node with data val at end
    def push_back(self, value):
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next # find last element of list
            curr.next = Node(value)
    
    # removes first Node; returns new head
    def pop_front(self):
        if self.head:
            dummy = Node(0)
            dummy.next = self.head.next
            self.head = dummy.next
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
        # edge case: i > length of list
        if i > self.length():
            return
        if i == 0: 
            self.pop_front()
        prev, curr = self.head, self.head
        count = 0
        while count != i:
            prev = curr
            curr = curr.next
            count += 1
        if curr.next:
            prev.next = curr.next
        else:
            prev.next = None
    
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
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
    
    # reverses Linked List recursively
    def reverseRecursive(self, head):
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseRecursive(head.next)
            head.next.next = head
        head.next = None
        return newHead
        
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
    list = SinglyLinkedList()

    list.push_front(2) # | 2 |
    list.push_front(3) # | 3 | 2 |
    list.push_back(6)  # | 3 | 2 | 6 |
    list.push_back(7)  # | 3 | 2 | 6 | 7 |
    list.push_back(8)  # | 3 | 2 | 6 | 7 | 8 |
    list.pop_front()   # | 2 | 6 | 7 | 8 |
    list.pop_back()    # | 2 | 6 | 7 |
    list.pop_node(1)   # | 2 | 7 |
    list.print()

main()

