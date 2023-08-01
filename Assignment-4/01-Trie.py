"""
Raina Wan
06-28-2023

Build a Trie:
Implement a trie class, including the insert, search, and delete methods.

Time Spent:
30 minutes
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for i in word:
            # if not in trie yet, add to dict
            if i not in curr.children:
                curr.children[i] = TrieNode()

            # move pointer to current char
            curr = curr.children[i]
        
        curr.end = True
    
    def search(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.end
    
    def remove(self, word):
        curr = self.root
        for i in word:
            curr = curr.children[i]
        curr.end = False


if __name__ == "__main__":
    trie = Trie()
    trie.insert("coffee")
    trie.insert("tea")

    print(trie.search("coffee")) # Output: True
    print(trie.search("tea"))    # Output: True
    print(trie.search("te"))     # Output: False

    trie.remove("coffee")

    print(trie.search("coffee")) # Output: False