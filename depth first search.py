# Depth-First Search (DFS) implementation using adjacency list

# Representing the graph using a dictionary
graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}

# Function to perform DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(start)
    print(start, end=" ")

    # Recurse for all the neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Starting DFS from node 5
print("Depth-First Search traversal starting from node 5:")
dfs(graph, 5)




#output
Depth-First Search traversal starting from node 5:
5 3 2 4 8 7

