"""
Raina Wan
04-30-2023

Floor In BST:
Given a target numeric value and a binary search tree, return the 
floor (greatest element less than or equal to the target) in the BST.

Time Complexity: O(logn) => Traversing only right / left side of tree, depending on target and node
Space Complexity: O(1)

Technique: 
Search binary search tree (BST)

Time Spent:
35 minutes

Approach:
1) Base case: invalid node (return None) or leaf node (return node.val)
2) If node.val == target, it is the greatest element equal to target. Return node
3) If node.val > target, need to find element less than current node. Traverse left tree
4) If node.val < target, there may be a greater element found in right subtree. Traverse right tree
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def floor_in_bst(node, target):
    if not node.left and not node.right:
        return node.val
    if not node:
        return -1
    
    if node.val == target:
        return node.val
    elif node.val > target: # traverse left subtree
        res = floor_in_bst(node.left, target)
        return res
    elif node.val < target: # traverse right subtree
        res = floor_in_bst(node.right, target)
        return res


def main():
    node20 = Node(20, None, None)
    node17 = Node(17, None, node20)
    node13 = Node(13, None, None)
    node16 = Node(16, node13, node17)
    node9 = (9, None, None)
    node8 = (8, None, node9)
    root = Node(10, node8, node16)

    print(floor_in_bst(root, 13)) # Output : 13
    print(floor_in_bst(root, 15)) # Output : 13

main()
