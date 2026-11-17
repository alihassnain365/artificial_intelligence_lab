# Graph representation
# Each node contains neighbours and the cost to reach them
graph = {
    'S': {'A': 3, 'C': 5, 'D': 7},
    'A': {},
    'B': {'E': 9},
    'C': {'F': 11},
    'D': {'B': 13, 'G': 15},
    'E': {'G': 17},
    'F': {'E': 19, 'G': 21},
    'G': {}
}

# Uniform Cost Search Function
def UniformCostSearch(startingNode, goal, myGraph):
    cost = 0  # initial cost from the start node
    path = [startingNode]  # path starts from the starting node
    visited = []  # list to store visited (explored) nodes

    # Queue structure:
    # even index = cost, odd index = corresponding path
    # example: [3, ['S','A'], 2, ['S','C']]
    queue = [cost, path]

    while queue:  # loop runs until the queue becomes empty
        index = 0
        minIndex = 0

        # find the path with the SMALLEST COST g(n)
        while index < len(queue):
            if queue[minIndex] > queue[index]:  # compare costs
                minIndex = index
            index = index + 2  # move to next cost-path pair

        cost = queue.pop(minIndex)  # remove the smallest cost
        path = queue.pop(minIndex)  # remove its corresponding path
        last_visited = path[-1]  # last node in the path

        if last_visited not in visited:
            visited.append(last_visited)

            # goal test
            if last_visited == goal:
                print("Order of nodes added to the explored set:", visited)
                path.append(cost)  # add the total cost at the end of the path
                return path

            # expand the neighbours of the current node
            for child in myGraph[last_visited].keys():
                newPath = list(path)  # copy of the current path
                newPath.append(child)  # add the child node to the path
                queue.append(cost + myGraph[last_visited][child])  # new cost
                queue.append(newPath)  # new path


print(UniformCostSearch('S', 'G', graph))