"""
Raina Wan
06-07-2023

Road Networks:
In some states, it is not possible to drive between any two towns because they are not connected to the 
same road network. Given a list of towns and a list of pairs representing roads between towns, return the 
number of road networks. (For example, a state in which all towns are connected by roads has 1 road network,
and a state in which none of the towns are connected by roads has 0 road networks.)

Time Complexity: T(n + m) => visit each town and road 
Space Complexity: T(n + m) => creating map with n cities and m roads

Technique:
Depth-first search

Time Spent:
35 minutes

Approach:
1) Create map of connecting cities
2) Traverse through each town, added to set. If connecting city,
   keep traversing. Otherwise, increase count (indicating disconnecting city)
"""

from collections import defaultdict

def road_networks(towns, roads):
    # create dictionary for connecting roads
    networks = defaultdict(list)
    for i, j in roads:
        networks[i].append(j)
        networks[j].append(i)
    
    visited = set()
    count = 0

    def dfs(town):
        visited.add(town)
        for n in networks[town]:
            if n not in visited:
                dfs(n)
    
    for town in networks:
        if town not in visited:
            count += 1
            dfs(town)
    
    return count

if __name__ == "__main__":
    print(road_networks(
        ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", 
        "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"],
        [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), 
        ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), 
        ("Healy", "Anchorage")]
    ))
    # Output: 2
    # Networks: Gustavus - GlacierBay
    #           Anchorage - Fairbanks - McCarthy - CopperCenter - Homer - Healy

    print(road_networks(
        ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], 
        [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), 
        ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    ))
    # Output: 3
    # Networks: Kona - Hilo - Volcano
    #           Haiku - Kahului - Lahaina - Hana
    #           Lihue - Waimea - Princeville
    

"""
{
    "Anchorage" : ["Homer", "Copper Center", "Healy", "Homer"],
    "Glacier Bay" : ["Gustavus"],
    "Copper Center" : ["McCarthy", "Fairbanks", "Anchorage"],
    "Healy" : ["Fairbanks", "Anchorage"]
    "Homer" : ["Anchorage"],
    "Gustavus" : ["Glacier Bay"],
    "McCarthy" : ["Copper Center"],
    "Fairbanks" : ["Copper Center", "Healy"],
}
"""
