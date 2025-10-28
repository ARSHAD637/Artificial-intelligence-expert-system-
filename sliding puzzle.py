import heapq

# Define the goal state
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the empty space

# Get the position of the blank (0)
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

# Compute the heuristic (Manhattan distance)
def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Convert list of lists to tuple (hashable form for visited)
def puzzle_to_tuple(puzzle):
    return tuple(tuple(row) for row in puzzle)

# Generate all possible moves
def get_neighbors(puzzle):
    x, y = find_blank(puzzle)
    moves = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[x][y], new_puzzle[nx][ny] = new_puzzle[nx][ny], new_puzzle[x][y]
            moves.append(new_puzzle)
    return moves

# A* Search Algorithm
def a_star(start):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (manhattan_distance(start), 0, start, []))

    while priority_queue:
        _, cost, puzzle, path = heapq.heappop(priority_queue)
        state_tuple = puzzle_to_tuple(puzzle)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if puzzle == GOAL_STATE:
            return path + [puzzle]

        for neighbor in get_neighbors(puzzle):
            heapq.heappush(priority_queue, (
                cost + 1 + manhattan_distance(neighbor),
                cost + 1,
                neighbor,
                path + [puzzle]
            ))
    return None

# Display the puzzle grid
def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

# Example: Scrambled initial state
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

print("🧩 Initial State:")
print_puzzle(initial_state)

solution = a_star(initial_state)

if solution:
    print("✅ Solution found! Steps:")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        print_puzzle(state)
else:
    print("❌ No solution found.")

#output:
#🧩 Initial State:
#1 2 3
#4   6
#7 5 8

#✅ Solution found! Steps:
#Step 0:
#1 2 3
#4   6
#7 5 8

#Step 1:
#1 2 3
#4 5 6
#7   8

#Step 2:
#1 2 3
#4 5 6
#7 8

