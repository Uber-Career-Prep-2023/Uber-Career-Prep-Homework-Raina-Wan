"""
Raina Wan
03-01-2023

Shortest Substring:
Given a string and a second string representing required characters, return the 
length of the shortest substring containing all the required characters.

Time Complexity: O(n) => going through every character in input string
Space Complexity: O(n) => storing character count of both strings into separate dictionaries

Technique: Two-Pointer "Catch-Up" Condition

Time Spent:
40 minutes

Approach:
1) Create hashmap of required substring letters.
2) Iterate through input string until count of input letters matches required letters.
3) Keep track of the minimum length. While string is still valid, delete from left window.
"""

def ShortestSubstring(input, substr):

    res = float("inf")
    window, required = {}, {}

    # create map of required substring characters
    for i in substr:
        if i in required:
            required[i] += 1
        else:
            required[i] = 1

    curr, req = 0, len(required)
    left = 0

    for right in range(len(input)):
        # create map of current window
        if input[right] in window:
            window[input[right]] += 1
        else:
            window[input[right]] = 1

        # update current count if one of required letters
        if input[right] in required and window[input[right]] == required[input[right]]:
            curr += 1
        
        while curr == req:
            res = min(res, right - left + 1)
            # keep popping from left of window until invalid substring
            window[input[left]] -= 1 
            if input[left] in required and window[input[left]] < required[input[left]]:
                curr -= 1
            left += 1

    return res

def main():
    print(ShortestSubstring("abracadabra","abc")) # Output: 4
    print(ShortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx","zzyzx")) # Output: 10
    print(ShortestSubstring("dog","god")) # Output: 3

main()
