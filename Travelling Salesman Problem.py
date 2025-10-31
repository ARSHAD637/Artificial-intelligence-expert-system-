import numpy as np
import random

# Parameters
cities = [(0,0), (1,5), (5,2), (7,5), (8,2), (2,7)]
n = len(cities)
dist = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        dist[i][j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))

num_ants = 10
num_iter = 100
alpha = 1      # pheromone influence
beta = 2       # heuristic influence
rho = 0.1      # evaporation rate

# Initialize pheromones
pher = np.ones((n,n))

def probability(from_city, available):
    den = sum((pher[from_city][j]**alpha) * ((1/dist[from_city][j])**beta) for j in available)
    return [((pher[from_city][j]**alpha) * ((1/dist[from_city][j])**beta))/den for j in available]

def build_tour():
    tour = [random.randint(0,n-1)]
    available = set(range(n)) - {tour[0]}
    while available:
        probs = probability(tour[-1], list(available))
        next_c = random.choices(list(available), weights=probs, k=1)[0]
        tour.append(next_c)
        available.remove(next_c)
    return tour

def total_cost(tour):
    return sum(dist[tour[i]][tour[(i+1)%n]] for i in range(n))

best_tour = None
best_cost = float("inf")

for it in range(num_iter):
    tours = [build_tour() for _ in range(num_ants)]
    costs = [total_cost(t) for t in tours]
    # Evaporate pheromones
    pher *= (1 - rho)
    # Reinforce best paths
    for t, cost in zip(tours, costs):
        for i in range(n):
            pher[t[i]][t[(i+1)%n]] += 1.0/cost
    min_idx = np.argmin(costs)
    if costs[min_idx] < best_cost:
        best_cost = costs[min_idx]
        best_tour = tours[min_idx]

print("Best tour found:", best_tour)
print("Best tour path:", [f"City {i}" for i in best_tour])
print("Total cost:", round(best_cost, 2))
