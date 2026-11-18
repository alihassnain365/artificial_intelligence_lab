graph = {
    'S': {'A': 2, 'B': 5, 'C': 1},
    'A': {'D': 4, 'E': 3},
    'B': {'F': 2},
    'C': {'G': 10},
    'D': {},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}
heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 4,
    'D': 5,
    'E': 1,
    'F': 3,
    'G': 0
}

def gbfs(start, goal,graph,heuristic):
    frontier = list()
    visited = list()
    frontier.append((heuristic[start],[start])) # list of tuples (hn,path)
    while frontier:
        # finding the tuple(hn,path) with minimum hn
        min_index = 0
        for i in range(len(frontier)):
            if frontier[i][0] < frontier[min_index][0]:
                min_index = i
        # we got the index on which the min hn is available
        hn,path = frontier.pop(min_index)
        current_node = path[-1];
        if current_node in visited:
            continue
        if current_node == goal:
            return visited,path
        visited.append(current_node)
        # now getting the neighbours of the current node
        neighbours = graph[current_node] # {key:value} -> ignore value here as it is cost
        for neighbour in neighbours:
            if neighbour not in visited:
                frontier.append((heuristic[neighbour],path + [neighbour]))
    return visited,None

visited, path = gbfs('S', 'G', graph=graph, heuristic=heuristic)
print(visited)
print(path)


