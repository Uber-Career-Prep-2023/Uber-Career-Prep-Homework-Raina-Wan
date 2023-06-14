"""
Raina Wan
06-14-2023

Prerequisite Courses:
Given a list of courses that a student needs to take to complete their major 
and a map of courses to their prerequisites, return a valid order for them to 
take their courses assuming they only take one course for their major at once.

Time Complexity: O(V + E) => must visit every course (vertex) and its prereq (edge) 
Space Complexity: O(V + E) => must store visited courses in set

Technique: 
Depth-first search

Time Spent:
40 minutes

Approach:
1) Make sure map has all courses and their prerequisites (no prereqs == empty list).
2) Add visited courses to set. Create path to keep track of course order.
3) Use dfs to recursively locate any prereq classes.
4) Return order of classes.
"""

def prerequisite_courses(courses, prereqs):
    for i in courses:
        if i not in prereqs:
            prereqs[i] = []

    order = []
    visited = set()
    path = set()
    
    def dfs(course):
        if course in visited or path: # already visited course
            return 
        
        visited.add(course)
        path.add(course)

        # visit all prereqs before adding curr course to order[]
        for i in prereqs[course]:
            dfs(i)
        
        order.append(course)
        path.remove(course)
        
    for i in courses:
        dfs(i)

    print(order)
    return order


if __name__ == "__main__":

    prerequisite_courses(["Intro to Programming", "Data Structures", 
                        "Advanced Algorithms", "Operating Systems", "Databases"], 
                        { "Data Structures": ["Intro to Programming"], 
                        "Advanced Algorithms": ["Data Structures"], 
                        "Operating Systems": ["Advanced Algorithms"], 
                        "Databases": ["Advanced Algorithms"] })
    # Output: ['Intro to Programming', 'Data Structures', 'Advanced Algorithms', 'Operating Systems', 'Databases']

    prerequisite_courses(["Intro to Writing", "Contemporary Literature", 
                        "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], 
                        { "Contemporary Literature": ["Intro to Writing"], 
                        "Ancient Literature": ["Intro to Writing"], 
                        "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], 
                        "Plays & Screenplays": ["Intro to Writing"] })
    # Output: ['Intro to Writing', 'Contemporary Literature', 'Ancient Literature', 'Comparative Literature', 'Plays & Screenplays']
