"""
Raina Wan
04-22-2023

Copy Tree:
Given a binary tree, create a deep copy. Return the root of the new tree.

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
Breadth First Search

Time Spent:
35 minutes
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def CopyTree(root):
    if not root:
        return None
    else:
        copy = Node(root.val)
        copy.left = CopyTree(root.left)
        copy.right = CopyTree(root.right)
        return copy

def print_tree(res, root):
    res.append(root.val)
    if root.left:
        print_tree(res, root.left)
    if root.right:
        print_tree(res, root.right)
    return res

def main():
    node1 = Node(2)
    node2 = Node(5)
    node3 = Node(8)
    node4 = Node(1)
    node5 = Node(4)
    node6 = Node(7)
    node7 = Node(3)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    root = node1
    deep_copy = CopyTree(root)
    
    print(print_tree([], deep_copy)) # Output: [2, 5, 1, 4, 8, 7, 3]
    print(print_tree([], root))      # Output: [2, 5, 1, 4, 8, 7, 3]


main()
