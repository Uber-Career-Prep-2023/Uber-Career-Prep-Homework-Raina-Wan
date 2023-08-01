"""
Raina Wan
07-05-2023

Boggle:
Boggle is a word game in which players compete to find the most words on a square grid of random
letters. Valid words must be at least three characters and formed from non-overlapping (i.e., a
position on the board can only be used once in a word) adjacent (including diagonal) letters. 
Given a Boggle board and a dictionary of valid words, return all valid words on the board.

Time Complexity: O(m*n) => going through all letters in board and in trie.
Space Complexity: O(n*k) => creating trie with n nodes and k pointers.

Technique:
Trie, backtrack

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


def boggle(valid_words, board):
    trie = Trie()
    ROW, COL = len(board), len(board[0])
    visited = set()
    res = []

    # create trie of valid words
    for i in valid_words:
        trie.insert(i.upper())

    def backtrack(i, j, word): 
        if i < 0 or j < 0 or i >= ROW or j >= COL:
            return 
        if (i, j) in visited: # no repeat letters
            return 

        word += board[i][j]

        # valid word
        if trie.search(word):
            res.append(word)

        visited.add((i, j))
        
        backtrack(i, j+1, word) 
        backtrack(i+1, j, word)
        backtrack(i, j-1, word)
        backtrack(i-1, j, word)
        backtrack(i+1, j+1, word) 
        backtrack(i-1, j-1, word)
        backtrack(i-1, j+1, word)
        backtrack(i+1, j-1, word)

        # remove curr letter so can append root's neighbors to root
        visited.remove((i, j))

    for r in range(ROW):
        for c in range(COL):
            backtrack(r, c, "")
    
    return res
    
    


if __name__ == "__main__":
    words = ["Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", 
    "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Rap", 
    "Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"]

    board = [
            ["A", "D", "E"],
            ["R", "C", "P"],
            ["L", "A", "Y"]
            ]

    print(boggle(words, board))
    # Output: ['ACE', 'RAY', 'RAP', 'CAPE', 'CLAY', 'CLAP', 'PAY', 
    #          'PACE', 'LAY', 'LACE', 'LAP', 'ACE', 'APE', 'YAP']
