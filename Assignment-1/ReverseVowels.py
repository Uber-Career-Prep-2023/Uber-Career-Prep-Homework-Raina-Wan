"""
Raina Wan
01-31-2023

Reverse Vowels:
Given a string, reverse the order of the vowels in the string.

Time Complexity: O(n) => iterating through word twice equates to O(2n)
Space Complexity: O(n) => creating a list fo the word, stack, and vowels equates to O(3n)

Technique: 
Stack

Time Spent:
35 minutes

Approach:
Iterate through word and push all vowels into a stack
Iterate through word again. Upon finding vowel, replace it with top of stack. Pop stack
"""

def reverse_vowels(word):
    word = list(word)
    stack = []
    vowels = ['a','e','i','o','u']

    for i in word:
        if i.lower() in vowels:
            stack.append(i)

    for i in range(len(word)):
        if word[i].lower() in vowels:
            word[i] = stack.pop()

    print("".join(word))
    return "".join(word)

def main():
    reverse_vowels("Uber Career Prep")  # eber Ceraer PrUp
    reverse_vowels("xyz")               # xyz
    reverse_vowels("flamingo")          # flominga

main()
