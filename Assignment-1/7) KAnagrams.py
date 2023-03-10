"""
Raina Wan
03-09-2023

KAnagrams:
Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k 
characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.

Time Complexity: O(3n) => Traversing through both strings to create map then first map to compare characters
Space Complexity: O(2n) => Using two maps to create string occurrences

Technique:
Simultaneous Iteration Two-Pointer

Time Spent:
30 minutes

Approach:
1) Create two maps, counting the occurrence of each character in both strings
2) Iterate through the first map
3) If a letter is missing in the second map, add that many occurrences to counter
4) If the values are not equal, add the absolute value of the difference to the counter
5) If at any point the counter exceeds k (meaning we have exceeded the number of max changes), return False
"""

def KAnagrams(s1, s2, k):
    if len(s1) != len(s2): return False
    map1, map2 = {}, {}
    count = 0

    # create occurrence of letters
    for i in s1:
        if i in map1:
            map1[i] += 1
        else:
            map1[i] = 1

    for i in s2:
        if i in map2:
            map2[i] += 1
        else:
            map2[i] = 1

    # look through letters in first map
    for key in map1:
        if key not in map2: # s1 has letter that s2 doesnt
            count = count + map1[key]
            continue
        if map1[key] != map2[key]: # get difference between two letters
            count = count + abs(map1[key] - map2[key])
        if count > k: # if at point count exceeds max changes, return false
            return False

    return True

def main():
    print(KAnagrams("apple", "peach", 1)) # Output: False
    print(KAnagrams("apple", "peach", 2))  # Output: True
    print(KAnagrams("cat", "dog", 3))  # Output: True
    print(KAnagrams("debit curd", "bad credit", 1))  # Output: True
    print(KAnagrams("baseball", "basketball", 2))  # Output: False

main()
