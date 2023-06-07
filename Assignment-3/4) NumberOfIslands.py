"""
Raina Wan
06-04-2023

Number of Islands:
Given a binary matrix in which 1s represent land and 0s represent water. 
Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).

Time Complexity: O(m x n) => have to visit every box in the grid
Space Complexity: O(1) => only storing number of islands

Technique:
Depth-first search

Time Spent:
30 minutes

Approach:
1) Visit every box in the grid until a 1 (land) is reached
2) Find all neighboring 1s by marking visited 1s
3) Increment the number of islands
"""


def num_islands(board):

    ROWS, COLS = len(board), len(board[0])
    count = 0

    def dfs(row, col):
        # return if not connecting square
        if row >= ROWS or row < 0 or col >= COLS or col < 0:
            return
        if board[row][col] != 1:
            return
        # mark neighboring islands so won't revisit
        board[row][col] = 'X'
        
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
        
    
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                count += 1
                dfs(r, c)

    return count


def main():
    board = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    print(num_islands(board)) # Output: 3

    board = [
        [1, 0, 0],
        [0, 0, 0]
    ]
    print(num_islands(board)) # Output: 1

main()
