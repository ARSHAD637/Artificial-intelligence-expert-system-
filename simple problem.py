import random
import math

# Define tasks and time slots
tasks = ['Task1', 'Task2', 'Task3', 'Task4', 'Task5', 'Task6']
slots = ['Slot1', 'Slot2', 'Slot3']
slot_capacity = 2  # Max tasks per slot

# Generate a random initial schedule (assignment of tasks to slots)
def random_schedule(tasks, slots):
    return [random.choice(slots) for _ in tasks]

# Cost function: penalize overflow in any slot (over slot_capacity)
def cost(schedule):
    counts = {slot: 0 for slot in slots}
    for slot in schedule:
        counts[slot] += 1
    penalty = 0
    for cnt in counts.values():
        if cnt > slot_capacity:
            penalty += (cnt - slot_capacity)
    return penalty

# Neighbor: randomly move one task to a different slot
def neighbor(schedule):
    new_schedule = schedule[:]
    idx = random.randrange(len(tasks))
    available_slots = [slot for slot in slots if slot != new_schedule[idx]]
    new_schedule[idx] = random.choice(available_slots)
    return new_schedule

# Simulated Annealing
def simulated_annealing(tasks, slots, slot_capacity, T=100, T_min=1e-3, alpha=0.95):
    current = random_schedule(tasks, slots)
    current_cost = cost(current)
    best = current[:]
    best_cost = current_cost
    while T > T_min and best_cost > 0:  # Stop if perfect schedule found
        candidate = neighbor(current)
        candidate_cost = cost(candidate)
        dE = candidate_cost - current_cost
        if dE < 0 or random.uniform(0, 1) < math.exp(-dE / T):
            current = candidate
            current_cost = candidate_cost
            if current_cost < best_cost:
                best = current[:]
                best_cost = current_cost
        T *= alpha  # Cooling schedule
    return best, best_cost

best_schedule, best_cost = simulated_annealing(tasks, slots, slot_capacity)
print("Best schedule found:")
for t, s in zip(tasks, best_schedule):
    print(f"{t} -> {s}")
print("Cost (conflicts):", best_cost)
