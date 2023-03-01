"""
Raina Wan
02-28-2023

Backspace String Compare:
Given two strings representing series of keystrokes, determine whether the resulting text is 
the same. Backspaces are represented by the '#' character so "x#" results in the empty string ("").

Time Complexity: O(2n) => iterating through two strings
Space Complexity: O(2n) => using two lists to store modified string

Technique: Stack + Simultaneous Iteration Two Pointers

Time Spent:
35 minutes

Approach:
1) Create two separate stacks
2) Iterate through each string. If backspace '#' is found, pop top of stack
3) Compare both stacks. Return true if they are equal, false otherwise

"""

def BackspaceStringCompare(first, second):
    if not first and not second: return True
    if not first or not second: return False

    stack_one, stack_two = [], []

    for i in first:
        if i == "#":
            if stack_one: # edge case: cannot remove from empty stack
                stack_one.pop()
        else:
            stack_one.append(i)
    
    for i in second:
        if i == "#":
            if stack_two:
                stack_two.pop()
        else:
            stack_two.append(i)

    return stack_one == stack_two

def main():
    print(BackspaceStringCompare("abcde","abcde"))                           # Output: True
    print(BackspaceStringCompare("Uber Career Prep","u#Uber Careee#r Prep")) # Output: True
    print(BackspaceStringCompare("abcdef###xyz","abcw#xyz"))                 # Output: True
    print(BackspaceStringCompare("abcdef###xyz","abcdefxyz###"))             # Output: False

main()
