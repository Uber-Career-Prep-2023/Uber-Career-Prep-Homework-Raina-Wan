"""
Raina Wan
04-30-2023

Left View:
Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.

Time Complexity: O(n) => Add every node inside queue
Space Complexity: O(n) => result can be up to size of tree

Technique:
Level-order (breadth-first) traversal

Time Spent:
40 minutes

Approach:
1) Create a queue and add the root.
2) Within the length of the queue, pop the leftmost node and add its right child then left child (order matters).
3) Add node to result.
"""


import collections

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_view(root):
    if not root:
        return None
    
    res = []
    q = collections.deque([root])
    
    while q:
        left_side = None
        for i in range(len(q)):
            node = q.popleft()
            if node:
                left_side = node
                q.append(node.right)
                q.append(node.left)
        
        if left_side:
            res.append(left_side.val)
    
    return res


def main():
    node15 = Node(15)
    node14 = Node(14, None, node15)
    node13 = Node(13, node14, None)
    node20 = Node(20)
    node9 = Node(9, node20, None)
    node3 = Node(3, node9, node13)
    node8 = Node(8)
    root = Node(7, node8, node3)

    print(left_view(root))
    # Output: [7, 8, 9, 20, 15]

main()
