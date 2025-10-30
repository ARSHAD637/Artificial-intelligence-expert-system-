import random

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def calculate_cost(state):
    """Number of attacking pairs of queens."""
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def get_best_neighbor(state):
    n = len(state)
    best_state = list(state)
    best_cost = calculate_cost(state)

    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                new_cost = calculate_cost(new_state)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_state = new_state
    return best_state, best_cost

def hill_climbing(n, max_restarts=100):
    for restart in range(max_restarts):
        # Step a: Random initial state
        current_state = [random.randint(0, n - 1) for _ in range(n)]
        current_cost = calculate_cost(current_state)

        while True:
            # Step c & d: Generate neighbors and move to best neighbor
            neighbor, neighbor_cost = get_best_neighbor(current_state)

            # Step e: Stop if no better neighbor
            if neighbor_cost >= current_cost:
                break

            current_state, current_cost = neighbor, neighbor_cost

        # If solution found, print and stop
        if current_cost == 0:
            print(f"✅ Solution found after {restart+1} restart(s):")
            print_board(current_state)
            print(f"Final Cost: {current_cost}")
            return current_state

    print("❌ No solution found after random restarts.")
    print(f"Last tried board (Cost = {current_cost}):")
    print_board(current_state)
    return None

# Run program
if __name__ == "__main__":
    N = int(input("Enter number of queens (e.g., 8): "))
    hill_climbing(N, max_restarts=50)
