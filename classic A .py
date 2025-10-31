from queue import PriorityQueue

# Graph with weighted edges
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 3, 'E': 5},
    'C': {'A': 4, 'F': 2},
    'D': {'B': 3, 'E': 1, 'F': 1},
    'E': {'B': 5, 'D': 1, 'F': 2},
    'F': {'C': 2, 'D': 1, 'E': 2}
}

# Heuristic values (straight-line or estimated cost to reach goal F)
# These are arbitrary for demonstration (smaller = closer to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

def a_star_search(start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    
    visited_order = []
    
    while not open_list.empty():
        _, current = open_list.get()
        visited_order.append(current)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            print("\nOrder of node expansion:", visited_order)
            print("Optimal Path:", " → ".join(path))
            print("Total Cost:", g_score[goal])
            return
        
        for neighbor, cost in graph[current].items():
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]
                open_list.put((f_score[neighbor], neighbor))

# Run A* Search
a_star_search('A', 'F')
