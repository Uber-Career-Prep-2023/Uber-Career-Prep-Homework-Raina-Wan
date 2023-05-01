"""
Raina Wan
04-26-2023

Move Nth Last To Front:
Given a singly linked list, move the nth from the last element to the front of the list.

Time Complexity: O(2n) => Identify length of list, traverse again to locate nth node from last
Space Complexity: O(1)

Technique:
Fixed- Distance Two-Pointer

Time Spent:
30 minutes

Approach:
1) Find length of list
2) To locate nth node, subtract length from n
3) Move curr pointer to nth node and prev to the node before
4) Set prev's next to curr's next and the nth node's next to head
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def move_nth_to_front(head, n):
    if not head:
        return None
    
    # find length of list
    curr = head
    count = 1
    while curr.next:
        count += 1
        curr = curr.next
    
    if n > count: # edge case: n out of bounds
        return None
    
    # to identify nth from the last element, subtract len - n
    i, delete = 0, count - n
    dummy = Node(0)
    dummy.next = head
    prev, curr = dummy, head
    while i != delete:
        i += 1
        prev = curr
        curr = curr.next
    
    # move nth node to beginning
    prev.next = curr.next
    curr.next = head
    return curr


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
    node9 = Node(19)
    node8 = Node(6, node9)
    node7 = Node(11, node8)
    node6 = Node(9, node7)
    node5 = Node(20, node6)
    node4 = Node(7, node5)
    node3 = Node(8, node4)
    node2 = Node(2, node3)
    node1 = Node(15, node2)

    print_list(node1)   # Output: | 15 | 2 | 8 | 7 | 20 | 9 | 11 | 6 | 19 |
    new_list = move_nth_to_front(node1, 2) # Output: | 6 | 15 | 2 | 8 | 7 | 20 | 9 | 11 | 19 |
    new_list = move_nth_to_front(node1, 7) # Output: | 8 | 15 | 2 | 7 | 20 | 9 | 11 | 6 | 19 |

main()

