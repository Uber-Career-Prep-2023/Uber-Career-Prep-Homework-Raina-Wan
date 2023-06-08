"""
Raina Wan
06-07-2023

Reverse Words:
Given a string, return the string with the order of the space-separated words reversed

Time Complexity: O(n) => Going through all the letters in the input to find words
Space Complexity: O(n) => Adding all letters to stack

Technique:
Stack

Time Spent:
25 minutes

Approach:
1) Separate input string into whole words using split().
2) Add words into stack.
3) Pop top of stack and append to result list. 
"""

def reverse_words(input):
    stack, res = [], []
    input = input.split(' ') # identify words
    for i in input:
        stack.append(i) # append to stack
    while stack:
        res.append(stack.pop()) # add top of stack to res then pop
    return " ".join(res) 


def main():
    print(reverse_words("Uber Career Prep"))
    # Output: Prep Career Uber

    print(reverse_words("Emma lives in Brooklyn, New York."))
    # Output: York. New Brooklyn, in lives Emma

main()

