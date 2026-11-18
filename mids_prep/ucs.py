graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5, 'E': 10},
    'C': {'B': 1, 'F': 7},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'E': 2, 'G': 8},
    'G': {}
}

def ucs(start, goal, graph):
    visited = list()
    frontier = list()
    frontier.append((0,[start]))
    while frontier:
        # we have to find the minimum (cost,path) tuple record in our frontier
        min_index = 0
        for i in range(len(frontier)):
            if frontier[i][0] < frontier[min_index][0]:
                min_index = i
        cost,path = frontier.pop(min_index)
            
        node = path[-1]
        if node in visited:
            continue
        if node == goal:
            return cost,visited,path
        visited.append(node)

        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                new_cost = cost + graph[node][neighbour]
                new_path = path + [neighbour]
                frontier.append((new_cost,new_path))
    return 0,visited,None

cost,visited,path = ucs('A','G',graph=graph)
print(cost)
print(visited)
print(path)
