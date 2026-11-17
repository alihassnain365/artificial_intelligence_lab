import heapq
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

def ucs(start,goal,my_graph):
    priority_queue = []
    visited = list()
    heapq.heappush(priority_queue,(0,start,[start]))
    while priority_queue:
        cost,node,path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        if node == goal:
            return cost,visited,path
        visited.append(node)

        neighbours = my_graph[node]
        for neighbour,weight in neighbours:
            if neighbour not in visited:
                new_path = path + [neighbour]
                new_cost = cost + weight
                heapq.heappush(priority_queue,(new_cost,neighbour,new_path))
    return 0,visited,None
cost,visited,path = ucs('A', 'G',graph)

print("Path:", path)
print("Cost:", cost)