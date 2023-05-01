"""
Raina Wan
04-28-2023

Disconnect Cycle:
Given a singly linked list, disconnect the cycle, if one exists.

Time Complexity: O(n) => visit every node to see where cycle exists (if any)
Space Complexity: O(n) => storing nodes in hashmap

Technique:
Hash linked list nodes

Time Spent:
25 minutes

Approach:
1) Create hashmap to store linked list nodes.
2) If current node's next is not in hashmap, no cycle exists. Store current node in map
3) If current node's next is in hashmap, cycle exists. Set current's next to nullptr (discontinuing cycle)
"""



class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def disconnect_cycle(head):
    if not head:
        return None

    # store nodes in hash map
    visited = {}
    dummy = Node(0, head)
    curr = head
    while curr:
        if curr.next not in visited:
            visited[curr] = 1
            curr = curr.next
        else:
            curr.next = None
    
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
    node3 = Node(12)
    node6 = Node(4, node3)
    node5 = Node(11, node6)
    node4 = Node(9, node5)
    node3.next = node4
    node2 = Node(18, node3)
    node1 = Node(10, node2)

    # print_list(node1) # infinite loop

    disconnect_cycle(node1)
    print_list(node1)

main()

"""
 10 -> 18 -> 12 -> 9 -> 11 -> 4 
             ^________________|  
              
| 10 | 18 | 12 | 9 | 11 | 4 |
"""
