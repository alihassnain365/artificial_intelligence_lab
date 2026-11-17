from collections import deque

graph = {
    'Warehouse': [('Market', 4), ('Park', 2)],
    'Market': [('Bank', 3), ('School', 5)],
    'Park': [('School', 2), ('Station', 6)],
    'Bank': [('Hospital', 8)],
    'School': [('Hospital', 3)],
    'Station': [('Hospital', 2)],
    'Hospital': []
}

def BFS(start, goal):
    queue = deque()
    queue.append((start,[start],0))
    explored = list()

    while queue:
        node: str
        path: list[str]
        cost: int

        node,path,cost = queue.popleft()

        if node in explored:
            continue
        explored.append(node)

        if node == goal:
            return explored, path, cost

        neighbours = sorted(graph[node])

        for neighbour, weight in neighbours:
            if neighbour not in explored:
                new_path = path + [neighbour]
                new_cost = weight + cost
                queue.append((neighbour, new_path, new_cost))
    return explored,None, 0

explored, path, cost = BFS('Warehouse', 'Hospital')
print(explored)
print("->".join(path))
print(cost)
