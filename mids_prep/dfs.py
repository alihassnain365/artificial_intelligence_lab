graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G', 'H'],
    'F': ['I'],
    'G': [],
    'H': ['J'],
    'I': [],
    'J': []
}

def dfs(start,goal):
    stack = list()
    stack.append((start,[start]))
    visited = list()
    while stack:
        node,path = stack.pop()
        if node in visited:
            continue
        if node is goal:
            return node,path
        visited.append(node)

        neighbours = sorted(graph[node], reverse=True)
        for neighbour in neighbours:
            if neighbour not in visited:
                new_path = path + [neighbour]
                stack.append((neighbour,new_path))
    return visited,None

print(dfs('A','J'))