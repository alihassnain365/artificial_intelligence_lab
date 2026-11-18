graph = {
    'S': {'A': 2, 'B': 4, 'C': 3},
    'A': {'D': 5, 'E': 2},
    'B': {'F': 3},
    'C': {'F': 2, 'G': 9},
    'D': {'G': 3},
    'E': {'G': 4},
    'F': {'G': 2},
    'G': {}
}

heuristic = {
    'S': 6,
    'A': 4,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}


def a_star(start,goal,graph,heuristic):
    frontier = list()
    visited = list()
    frontier.append((heuristic[start],[start],0)) # tuple (fn,path,gn)
    while frontier:
        #finding the index where is min fn (fn,path)
        
        min_index = 0
        for i in range(len(frontier)):
            if frontier[i][0] < frontier[min_index][0]:
                min_index = i
        # now we got the tuple with min (fn,path)
        fn,path,cost = frontier.pop(min_index)
        current_node = path[-1]
        if current_node in visited:
            continue
        if current_node == goal:
            return visited,path,cost
        visited.append(current_node)

        # now getting the neighbours of current node
        neighbours = graph[current_node] # {key:value}
        for neighbour in neighbours:
            if neighbour not in visited:
                new_cost = cost + graph[current_node][neighbour]
                new_fn = new_cost + heuristic[neighbour]
                new_path = path + [neighbour]
                frontier.append((new_fn,new_path,new_cost))
    return visited,None,0

visited,path,cost =  a_star('S', 'G', graph, heuristic)
print(visited)
print(path)
print(cost)


