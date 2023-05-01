"""
Raina Wan
04-27-2023

Is Palindrome:
Given a doubly linked list, determine if it is a palindrome.

Time Complexity: O(n) => Traversing list twice: once to find length, second to determine if palindrome
Space Complexity: O(1)

Technique:
Doubly linked list forward-backward two-pointer

Time Spent:
30 minutes

Approach:
1) Find middle of list by dividing length by 2
2) If list is odd, set l & r pointers to same middle node
   If list is even, set l to left middle node, r to right middle node
3) Move pointers outward, checking if node values are equal. If not, return false
4) If end of list is reached, all values are equal. Return True
"""


class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def is_palindrome(head):
    if not head:
        return None

    # find length of list
    curr = head
    count = 1
    while curr.next:
        count += 1
        curr = curr.next

    # find middle node
    middle = count // 2
    i = 0
    l, r = head, head
    
    while i != middle:
        i += 1
        l = l.next
        r = r.next

    if count % 2 == 0: # even
        l = l.prev
        
    # move l & r pointers outwards
    while l and r:
        if l.val != r.val:
            return False
        l = l.prev
        r = r.next
    
    return True
    

def print_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print('| ', end="")
    for i in res: 
        print(i, end = " | ")

def main():
    node6 = Node(9)
    node5 = Node(7, node6)
    node4 = Node(4, node5)
    node3 = Node(2, node4)
    node2 = Node(7, node3)
    node1 = Node(9, node2, None)

    node6.prev = node5
    node5.prev = node4
    node4.prev = node3
    node3.prev = node2
    node2.prev = node1

    print_list(node1)
    print(is_palindrome(node1)) 

main()

"""
| 9 | 2 | 4 | 2 | 9 | 
True

| 9 | 12 | 4 | 2 | 9 | 
False

| 9 | 7 | 2 | 2 | 7 | 9 | 
True

| 9 | 7 | 2 | 4 | 7 | 9 | 
False
"""
