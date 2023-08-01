"""
Raina Wan
07-14-2023

Largest Square of 1s:
Given a square matrix of 0s and 1s, find the dimension of the largest square consisting only of 1s.

Time Complexity: O(m * n) => only searches grid from bottom right to top left
Space Complexity: O(m * n) => creating a cache that stores the max current dimension

Time Spent:
35 minutes
"""



def largest_square(grid):
    ROWS, COLS = len(grid), len(grid[0])
    cache = {} # (r, c) : square dimension

    def search(r, c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS:
            return 0

        if (r, c) not in cache:
            right = search(r, c + 1)
            bottom = search(r + 1, c)
            diag = search(r + 1, c + 1) # bottom right diag

            cache[(r, c)] = 0 # initially set value to 0
            if grid[r][c] == 1:
                # if there is a 0 in neighbors, max square is current square, 1
                # if all three have at least a 1, then max square is 1+1 = 2. a 2x2 grid
                cache[(r, c)] = 1 + min(right, bottom, diag)
        
        # cache is already filled. return it
        return cache[(r, c)]
    
    search(0, 0)

    # take the max of all the dimensions in our cache
    return max(cache.values())

if __name__ == "__main__":
    grid = [
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]
    ]
    print(largest_square(grid))
    # Output: 2 (bottom right square)

    grid = [
        [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0]
    ]
    print(largest_square(grid))
    # Output: 3 