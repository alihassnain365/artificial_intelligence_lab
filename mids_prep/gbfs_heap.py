import heapq
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

def gbfs(start,goal):
    priority_queue = []
    visited = list()
    heapq.heappush(priority_queue,(heuristic[start],start,[start]))
    while priority_queue:
        heu,node,path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        if node == goal:
            return visited,path
        visited.append(node)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                new_path = path + [neighbour]
                heapq.heappush(priority_queue,(heuristic[neighbour],neighbour,new_path))
    return visited,None

visited,path = gbfs('A','G')
print(visited)
print(path)