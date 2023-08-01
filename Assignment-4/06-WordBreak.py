"""
Raina Wan
07-15-2023

Word Break:
Given a string of characters without spaces and a dictionary of valid words, determine 
if it can be broken into a list of valid words by adding spaces. 

Time Complexity: O(m*n) => Searching full input string and each word in dictionary
Space Complexity: O(n) => dp of bool with size of input string

Time Spent:
30 minutes
"""

def word_break(input, words):
    dp = [False] * (len(input) + 1)   # initilize False to len of string + 1
    dp[len(input)] = True             # last char outside string is True

    for i in range(len(input) - 1, -1, -1):
        for w in words:
            # check if curr index compares to size of word
            if (i + len(w)) <= len(input):
                # check if substr matches word in dict
                if input[i : i + len(w)].lower() == w.lower():
                    dp[i] = dp[i + len(w)] # set position to be true thus far
            if dp[i]: # if already true, break out of words and go to next for loop iteration
                break
    
    return dp[0]

if __name__ == "__main__":
    words = ["Elf", "Go", "Golf", "Man", "Manatee",
             "Not", "Note", "Pig", "Quip", "Tee", "Teen"]

    print(word_break("mangolf", words)) 
    # Output: True (“man”, “golf”)

    print(word_break("manatee", words))
    # Output: True (“manatee”, “not”, “elf”)

    print(word_break("quipig", words))
    # Output: False


""" 
input = [m, a, n, g, o, l, f]
dp =    [f, f, f, f, f, f, f]
                           i
f != any word in dict

input = [m, a, n, g, o, l, f]
dp =    [f, f, f, t, f, f, f]
                  i
golf == golf. set dp to true

input = [m, a, n, g, o, l, f]
dp =    [t, f, f, t, f, f, f]
         i
man == man. set dp to true
"""