# # Graph representation
# # Each node contains its neighbours and the cost to reach them
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

# # Heuristic values h(n)
# # Estimated distance from each node to the goal
Heuristic = {
    'S': 20, 'A': 18, 'C': 16, 'D': 14,
    'B': 10, 'E': 9, 'F': 10, 'G': 0
}


# # Greedy Best First Search Function
# def GBFS(startingNode, goal, myGraph):
#     cost = 0  # initial cost is 0
#     path = [startingNode]  # path starts from the starting node
#     visited = []  # list to store visited (explored) nodes

#     # Queue structure:
#     # even index = cost, odd index = corresponding path
#     # example: [3, ['S', 'A'], 2, ['S', 'C']]
#     queue = [cost, path]

#     while queue:  # loop runs until the queue becomes empty
#         index = 0
#         minIndex = 0

#         # Find the path whose LAST NODE has the smallest heuristic h(n)
#         while index < len(queue):
#             # h(n) of the last node of the current minimum path
#             currentNode = Heuristic[queue[minIndex + 1][-1]]

#             # h(n) of the last node of the next path
#             nextNode = Heuristic[queue[index + 1][-1]]

#             if currentNode > nextNode:  # select the smaller heuristic
#                 minIndex = index

#             index = index + 2  # move to next cost-path pair

#         cost = queue.pop(minIndex)  # remove the cost of the chosen path
#         path = queue.pop(minIndex)  # remove the chosen path
#         last_visited = path[-1]  # last node in the path

#         if last_visited not in visited:  # add node to the visited list
#             visited.append(last_visited)

#             # Goal test
#             if last_visited == goal:
#                 print("Order of nodes added to the explored set:", visited)
#                 path.append(cost)  # add the total cost at the end of the path
#                 return path

#             # Expand the neighbours of the current node
#             for child in myGraph[last_visited].keys():
#                 newPath = list(path)  # copy of the current path
#                 newPath.append(child)  # add the child node to the path
#                 queue.append(cost + myGraph[last_visited][child])  # new cost
#                 queue.append(newPath)  # new path


# print(GBFS('S', 'G', graph))

def gbfs(start,goal,myGraph):
    cost = 0
    path = [start]
    visited = list()
    queue = [cost,path]
    while queue:
        index = 0
        min_index = 0
        while index < len(queue):
            current_node = Heuristic[queue[min_index+1][-1]]
            next_node = Heuristic[queue[index+1][-1]]
            if next_node < current_node:
                min_index = index
            index = index + 2
        cost = queue.pop(min_index)
        path = queue.pop(min_index)
        last_visited = path[-1]

        if last_visited not in visited:
            visited.append(last_visited)
            if last_visited == goal:
                print("The Order of explored Nodes: ")
                path.append(cost)
                print(path)
                return path
            


            