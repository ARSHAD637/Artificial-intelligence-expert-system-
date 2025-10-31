import heapq

# Graph as adjacency list: node -> list of (neighbor, cost)
graph = {
    'A': [('B', 4), ('F', 2)],
    'B': [('E', 5), ('G', 1)],
    'C': [('A', 3)],
    'D': [('B', 2), ('G', 2)],
    'E': [('G', 2)],
    'F': [('B', 1)],
    'G': []
}

def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [start])]  # (cost, node, path)
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))
    return None, float('inf')

def dijkstra(graph, start, goal):
    pq = [(0, start, [start])]
    visited = {}
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        for neighbor, edge_cost in graph[node]:
            heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))
    return None, float('inf')

start, goal = 'C', 'G'
ucs_path, ucs_cost = uniform_cost_search(graph, start, goal)
dij_path, dij_cost = dijkstra(graph, start, goal)

print("UCS Path:", ucs_path)
print("UCS Total Cost:", ucs_cost)
print("Dijkstra Path:", dij_path)
print("Dijkstra Total Cost:", dij_cost)
print("Optimality validated:", ucs_path == dij_path and ucs_cost == dij_cost)
