from collections import deque


graph = {
    'S': [('A', 1), ('B', 1), ('C', 1)],
    'A': [('D', 1), ('E', 1)],
    'B': [('E', 1), ('F', 1)],
    'C': [('F', 1)],
    'D': [('H', 1)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'H': [],
    'G': []
}

# def BFS(start, goal):
#     queue = deque()
#     queue.append((start,[start],0))
#     explored = list()

#     while queue:
#         node,path,cost = queue.popleft()
#         if node in explored:
#             continue
#         explored.append(node)

#         if node == goal:
#             return explored,path,cost

#         neighbours = sorted(graph[node])

#         for neighbour,weight in neighbours:
#             if neighbour not in explored:
#                 new_path = path + [neighbour]
#                 new_cost = weight + cost
#                 queue.append((neighbour,new_path,new_cost))
#     return explored,None,0 # if goal is not found




# explored,path,cost = BFS('S','G')
# print("Explored order : ",explored)
# print("Path is : ")
# print("->".join(path))
# print("Total cost: ", cost)


def bfs(start, goal):
    """
    1. create a queue
    2. add start to queue
    3. loop till the queue is empty
        -take element out from the queue
        -see if it is a goal - if it is return the path
        -see if the current node is in the visited list - if it is then skip
        -get the all neighbours of that node, see if the neibhours are already in visited or in current queue than skip
        -sort the neighbours
        -find the new weight and cost
        -add them to the queue
    """
    queue = deque()
    visited = list()
    queue.append((start,[start],0))
    while queue:
        node,path,cost = queue.popleft()
        if node==goal:
            return path,cost
        if node in visited:
            continue
        neighbours = sorted(graph[node])

        for neighbour,weight in neighbours:
            if neighbours not in visited:
                new_path = path + [node]
                new_cost = cost + weight
                queue.append((neighbour,new_path,new_cost))
        # if goal is not found
        return visited,None,0



