
graph = {
    'S': {'A': 3, 'C': 2, 'D': 2},
    'A': {},
    'B': {'E': 2},
    'C': {'F': 1},
    'D': {'B': 3, 'G': 8},
    'E': {'G': 2},
    'F': {'E': 0, 'G': 4},
    'G': {}
}

def dfs(start,goal):
    stack = list()
    visited = list()
    stack.append((start,[start],0))
    while stack:
        node,path,cost = stack.pop()
        if node in visited:
            continue
        if node==goal:
            return visited,path,cost
        visited.append(node)
        neighbours = sorted(graph[node].items(), reverse=True)
        for neighbour,weight in neighbours:
            if neighbour not in visited:
                new_path = path + [node]
                new_cost = weight + cost
                stack.append((neighbour,new_path,new_cost))
        # if goal not found
    return visited,None,0

visited,path,cost = dfs('S','G')
print(visited)
print("->".join(path))
print(cost)        
