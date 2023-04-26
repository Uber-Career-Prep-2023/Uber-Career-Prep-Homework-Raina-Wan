"""
Raina Wan
04-26-2022

Is Binary Search Tree:
Given a binary tree, determine if it is a binary search tree.

Time Complexity: O(n) => worst case: must visit all nodes to determine if BST
Space Complexity: O(n)

Technique:
Breadth First Search

Time Spent:
35 minutes

Approach:
1) If left node is greater than current node, invalid BST. Return False
2) If right node is less than current node, invalid BST. Return False
3) Otherwise, call BST on left and right nodes. Return True
"""



class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class IsBST():
    def isValid(self, root):
        
        def valid(node, left, right):
            if not node:
                return True
            if left > node.val or right < node.val:
                return False
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))

def main():
    node1 = Node(5)
    node2 = Node(4)
    node3 = Node(6)
    node1.left = node2
    node1.right = node3

    tree = IsBST()
    print(tree.isValid(node1)) # Output: True

    node4 = Node(9)
    node2.left = node4

    print(tree.isValid(node1)) # Output: False

main()
