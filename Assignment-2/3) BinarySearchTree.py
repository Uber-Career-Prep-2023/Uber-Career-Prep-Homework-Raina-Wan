"""
Raina Wan
04-20-2023

Binary Search Tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def min(self):
        if not self.left: return None
        curr = self.left
        while curr.left:
            curr = curr.left
        return curr.val
    
    def max(self):
        if not self.right: return None
        curr = self.right
        while curr.right:
            curr = curr.right
        return curr.val
    
    def contains(self, val):
        if val < self.val:
            if not self.left: 
                return False # traversed to end and doesn't exist
            else:
                return self.left.contains(val)
        elif val > self.val:
            if not self.right:
                return False
            else:
                return self.right.contains(val)
        else: # val == self.val
            return True
    
    def insert(self, val):
        if val < self.val:
            if not self.left:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = BST(val)
            else:
                self.right.insert(val)
    
    def delete(self, val):
        if val < self.val:
            if not self.left: return None # not found
            else: return self.left.delete(val)
        elif val > self.val:
            if not self.right: return None # not found
            else: return self.right.delete(val)
        else: # found
            if not self.right: # no children on right. replace with left
                return self.left
            elif not self.left:
                return self.right
            else: # both children present
                # replace curr node with smallest node on right side
                curr = self.right
                while curr.left:
                    curr = curr.left
                val = curr.val
        val = None
    

        

def main():
    tree = BST(6)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.delete(1)
    print(tree.min()) # 1
    print(tree.max()) # 9
    print(tree.contains(7)) # False
    print(tree.contains(9)) # True

main()
