import heapq
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 5)],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 3,
    'D': 4,
    'E': 1,
    'F': 2,
    'G': 0
}

def a_star(start,goal,heurisitc,graph):
    priority_queue = []
    visited = set()
    heapq.heappush(priority_queue,(heuristic[start],start,[start]))
    while priority_queue:
        fn,node,path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        if node == goal:
            return visited,path
        visited.add(node)
        neighbours = graph[node]
        for neighbour,weight in neighbours:
            new_fn = heuristic[neighbour] + weight
            new_path = path + [neighbour]
            heapq.heappush(priority_queue,(new_fn,neighbour,new_path))
    return visited,None
visited,path = a_star('A','G',heuristic,graph)
print(visited)
print(path)

