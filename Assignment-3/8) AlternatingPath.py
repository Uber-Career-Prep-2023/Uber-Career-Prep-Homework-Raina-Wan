"""
Raina Wan
06-08-2023

Alternating Path:
Given an origin and a destination in a directed graph in which edges can be blue or red, determine the 
length of the shortest path from the origin to the destination in which the edges traversed alternate in 
color. Return -1 if no such path exists.

Time Complexity: O(n + m) => visiting all nodes and edges (start to end paths)
Space Complexity: O(n + m) => storing paths in dictionary

Technique:
Breadth-first search

Time Spent:
40 minutes

Approach:
1) Create a dictionary where the key is the origin and the value is a tuple containing dest and color (see bottom)
2) Create a queue that contains the current origin, length of the path thus far, and the color
3) If the origin matches the destination, we have found a valid path. Return the length
4) Otherwise, traverse through the origins' neighbors, but ONLY if the color is alternating
"""

from collections import defaultdict, deque

def alternating_path(paths, origin, destination):
    graph = defaultdict(list)
    for start, end, color in paths:
        graph[start].append((end, color))
    
    q = deque()
    q.append((origin, 0, None)) # current origin, length, color
    print(graph)
    while q:
        curr_origin, length, color = q.popleft()
        if curr_origin == destination:
            return length 
        for next_dest, next_color in graph[curr_origin]:
            if next_color != color:
                q.append((next_dest, length + 1, next_color))
    
    return -1
    

def main():
    print(alternating_path([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), 
                            ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), 
                            ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")], 
                            'A', 'E'))
    # Output: 4
    # Path: A→D (red), D→C (blue), C→B (red), B→E (blue))

    print(alternating_path([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), 
                            ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), 
                            ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")], 
                            'E', 'D'))
    # Output: -1
    # Invalid path: E→C (red), C→B (red), B→D (blue)


main()


"""
Graph = {
    'A': [('B', 'blue'), ('C', 'red'), ('D', 'red')], 
    'B': [('D', 'blue'), ('E', 'blue')], 
    'C': [('B', 'red')], 
    'D': [('C', 'blue'), ('E', 'red')], 
    'E': [('C', 'red')]
    }
"""
