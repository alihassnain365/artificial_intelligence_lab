from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H', 'I'],
    'F': [],
    'G': ['J'],
    'H': [],
    'I': ['J'],
    'J': []
}

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))
    visited = []

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        if node == goal:
            return path

        visited.append(node)

        neighbours = graph[node]

        for neighbour in neighbours:
            new_path = path + [neighbour]
            queue.append((neighbour, new_path))

    return None

print(bfs('A', 'J'))