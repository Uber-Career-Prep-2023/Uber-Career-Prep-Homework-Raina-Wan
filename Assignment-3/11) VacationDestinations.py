"""
Raina Wan
06-17-2023

Vacation Destinations:
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly 
from each other with corresponding travel times in hours, return the number of destinations within k 
hours of the origin. Assume that having a stopover in a city adds an hour of travel time.

Time Complexity: O(E*log(V^2)) => Traversing cities where every path has two cities 
Space Complexity: O(E + V) => Creating map of cities (vertices) and paths (edges)

Technique: 
BFS Graph Traversal

Time Spent:
40 minutes

Approach:
1) Create map where key is origin city and value is (destination, distance).
2) Create queue, appending the origin and current distance travelled.
3) Visit neighboring cities, adding the respective distance. Add new cities to res.
4) Continue until distance exceeds k
"""


from collections import defaultdict, deque

def vacation_destinations(cities, origin, k):
    travel_map = defaultdict(list)
    for start, end, dist in cities:
        travel_map[start].append((end, dist))
        travel_map[end].append((start, dist))

    q = deque([])
    q.append((origin, -1))
    visited = set()
    res = []

    while q:
        city, dist = q.popleft()
        if city in visited:
            continue
        visited.add(city)
        
        if dist != -1 and dist <= k:
            res.append(city)
        
        for neigh, distance in travel_map[city]:
            newDist = dist + distance + 1 # total distance + 1 hour travel time
            q.append((neigh, newDist))
    
    return (len(res), res)



if __name__ == "__main__":
    cities = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), 
              ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), 
              ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

    print(vacation_destinations(cities,"New York", 5))
    # Number of destinations: 2
    # Destinations: ['Boston', 'Philadelphia']

    print(vacation_destinations(cities,"New York", 7))
    # Number of destinations: 4
    # Destinations: ['Boston', 'Philadelphia', 'Newport', 'Washington, D.C.']

    print(vacation_destinations(cities,"New York", 8))
    # Number of destinations: 6
    # Destinations: ['Boston', 'Philadelphia', 'Newport', 'Portland', 'Washington, D.C.', "Harper's Ferry"]
