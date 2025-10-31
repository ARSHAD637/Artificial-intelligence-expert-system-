import itertools

# Define city names and the distance matrix (A, B, C, D)
cities = ['A', 'B', 'C', 'D']
distance = [
    [0, 10, 15, 20],  # Distances from A to A, B, C, D
    [10, 0, 35, 25],  # Distances from B to A, B, C, D
    [15, 35, 0, 30],  # Distances from C to A, B, C, D
    [20, 25, 30, 0]   # Distances from D to A, B, C, D
]

# Compute shortest route using brute force
def tsp_brute_force(distance, cities):
    n = len(cities)
    perms = itertools.permutations(range(1, n))
    min_path = []
    min_cost = float('inf')
    
    for perm in perms:
        cost = 0
        k = 0  # Start from city 0 (A)
        path = [k]
        for j in perm:
            cost += distance[k][j]
            path.append(j)
            k = j
        cost += distance[k][0]  # return to start
        path.append(0)
        if cost < min_cost:
            min_cost = cost
            min_path = path
    
    return [cities[i] for i in min_path], min_cost

path, cost = tsp_brute_force(distance, cities)
print("Shortest path:", path)
print("Minimum cost:", cost)
