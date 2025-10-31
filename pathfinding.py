import heapq

# Graph as adjacency list: node -> list of (neighbor, cost)
graph = {
    'A': [('B', 4), ('F', 2)],
    'B': [('E', 3), ('G', 1)],
    'C': [('A', 3)],
    'D': [('B', 2), ('G', 2)],
    'E': [('G', 2)],
    'F': [('B', 1)],
    'G': []
}

# Heuristic: straight-line distance to 'G'
heuristics = {
    'A': 4, 'B': 2, 'C': 6, 'D': 1, 'E': 2, 'F': 3, 'G': 0
}

def beam_search(graph, heuristics, start, goal, k):
    queue = [(0 + heuristics[start], 0, [start])] # (est. total cost, current cost, path)
    while queue:
        next_level = []
        for est_cost, curr_cost, path in queue:
            node = path[-1]
            if node == goal:
                return path, curr_cost
            for neighbor, edge_cost in graph[node]:
                if neighbor not in path:
                    cost = curr_cost + edge_cost
                    est_total = cost + heuristics[neighbor]
                    next_level.append((est_total, cost, path + [neighbor]))
        # Keep only k most promising nodes for next level
        queue = heapq.nsmallest(k, next_level)
    return None, None

def bfs(graph, start, goal):
    from collections import deque
    queue = deque([(start, [start], 0)])
    visited = set()
    while queue:
        node, path, cost = queue.popleft()
        if node == goal:
            return path, cost
        visited.add(node)
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], cost + edge_cost))
    return None, None

start, goal = 'C', 'G'
beam_width = 2

beam_path, beam_cost = beam_search(graph, heuristics, start, goal, beam_width)
bfs_path, bfs_cost = bfs(graph, start, goal)

print(f"Beam Search (width {beam_width}) path:", beam_path)
print(f"Beam Search cost:", beam_cost)
print("BFS path:", bfs_path)
print("BFS cost:", bfs_cost)
