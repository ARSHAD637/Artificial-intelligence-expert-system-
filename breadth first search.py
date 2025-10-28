from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    print("BFS Traversal Order:")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Graph represented as an adjacency list
graph = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 4],
    3: [0],
    4: [2]
}

# Start BFS from node 0
bfs(graph, 0)



output
BFS Traversal Order:
0 1 2 3 4 

