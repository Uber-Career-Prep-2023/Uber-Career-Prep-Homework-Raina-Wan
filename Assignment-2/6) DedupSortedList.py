"""
Raina Wan
04-26-2023

DedupSortedList:
Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

Time Complexity: O(n) => Traverse through every node to find duplicates
Space Complexity: O(1)

Technique:
Linked list fixed-distance two-pointer

Time Spent:
30 minutes

Approach:
Set prev pointer to dummy node and curr to head. 
If prev == curr, move curr forward and remove duplicate
Otherwise, move prev and curr forwards
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def dedup_sorted_list(head):
    if not head:
        return None
    
    dummy = Node()
    dummy.next = head
    prev, curr = dummy, head

    while curr:
        if prev.val == curr.val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    
    return dummy.next

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
    node9 = Node(10)
    node8 = Node(10, node9)
    node7 = Node(5, node8)
    node6 = Node(5, node7)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(2, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    print_list(node1) # Output: | 1 | 2 | 2 | 4 | 5 | 5 | 5 | 10 | 10 |
    print_list(dedup_sorted_list(node1)) # Output: | 1 | 2 | 4 | 5 | 10 |

    
    node13 = Node(8)
    node12 = Node(8, node13)
    node11 = Node(8, node12)
    node10 = Node(8, node11)

    print_list(node10)  # Output: | 8 | 8 | 8 | 8 |
    print_list(dedup_sorted_list(node10)) # Ouput: | 8 |

    
main()

