from collections import defaultdict
import collections

def create_graph(values):
    graph = defaultdict(list)
    for x, y in values:
        graph[x].append(y)
        if y not in graph:
            graph[y] = []
    return graph

def dfs(root, graph, visited):
    if root not in visited:
        visited.append(root)
        for neighbor in graph[root]:
            # if neighbor == target:
            #     return True
            dfs(neighbor, graph, visited)
    return visited
    # return False

def _dfs(target, graph):
    root = list(graph.keys())[0]
    visited = set()
    res = dfs(root, target, graph, visited)
    return res

def bfs(graph, root):
    q = collections.deque([root])
    visited = []
    while q:
        node = q.popleft()

        # add current node to visited to avoid repeat nodes
        if node not in visited:
            visited.append(node)

        # add unvisited neighbors to queue
        for i in graph[node]:
            if i not in visited:
                q.append(i)
    
    return visited

def add_edge(start, end, graph):
    graph[start].append(end)
    return graph

def print_graph(graph):
    for x in sorted(graph.keys()):
        print(x, ":", graph[x])

def main():
    graph = create_graph([(1, 2), (3, 2), (2, 3), (1, 3), (2, 0)])
    graph = add_edge(3, 5, graph)
    graph = add_edge(0, 2, graph)
    print_graph(graph)
    print(dfs(1, graph, []))
    print(bfs(graph, 1))

main()
