"""
Raina Wan
07-15-2023

Minimum Cost Stair Climbing:
You can only climb one or two stairs at once. The last stair you step on can be either 
stair n-1 or n-2. Given an array representing the costs per stair, what is the minimum 
possible toll you can pay to climb the staircase?

Time Complexity: O(n) => iterating through stairs backwards
Space Complexity: O(1)

Time Spent:
25 minutes
"""


def stair_climbing(stairs):
    stairs.append(0)  # final stair

    # iterate backwards to find min cost for each step
    # len(stairs) - 3 to start at second to last element
    for i in range(len(stairs) - 3, -1, -1):
        option1 = stairs[i] + stairs[i+1]
        option2 = stairs[i] + stairs[i+2]
        stairs[i] = min(option1, option2)

    # return min of first two values
    return min(stairs[0], stairs[1])


if __name__ == "__main__":
    print(stair_climbing([4, 1, 6, 3, 5, 8]))
    # Output: 9

    print(stair_climbing([11, 8, 3, 4, 9, 13, 10]))
    # Output: 25

"""
stairs = [4, 1, 6, 3, 5, 8] + [0]
last to first elem, calculate least amt of steps
[13,9,11,8,5,8]
min(13, 9) == 9
"""
