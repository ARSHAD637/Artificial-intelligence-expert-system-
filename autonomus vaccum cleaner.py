# Vacuum Cleaner AI Problem

import random
from collections import deque

# Define the grid
# 0 = clean cell, 1 = dirty cell, -1 = obstacle
grid = [
    [0, 1, 0, -1, 1],
    [0, 0, 1, 0, 0],
    [1, -1, 0, 1, 0],
    [0, 1, 0, 0, 1]
]

rows, cols = len(grid), len(grid[0])
start = (0, 0)  # starting position of vacuum

# Possible moves (Up, Down, Left, Right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_grid():
    for row in grid:
        print(row)
    print()

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != -1

def bfs(start, target):
    """Find shortest path from start to target."""
    queue = deque([(start, [])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == target:
            return path + [(x, y)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(x, y)]))
    return None

def find_dirty_cells():
    return [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 1]

def clean_environment(start):
    position = start
    steps = 0
    print("Initial Environment:")
    print_grid()

    while True:
        dirty_cells = find_dirty_cells()
        if not dirty_cells:
            print("✅ All cells are clean!")
            break

        # Find nearest dirty cell (shortest BFS path)
        shortest_path = None
        nearest_cell = None
        for cell in dirty_cells:
            path = bfs(position, cell)
            if path and (shortest_path is None or len(path) < len(shortest_path)):
                shortest_path = path
                nearest_cell = cell

        # Move along the shortest path
        for step in shortest_path[1:]:
            position = step
            steps += 1
            print(f"Vacuum moved to {position}")

        # Clean the cell
        grid[position[0]][position[1]] = 0
        print(f"Cleaned cell {position}")
        print_grid()

    print(f"Total movements: {steps}")

# Run the simulation
clean_environment(start)









output:
Initial Environment:
[0, 1, 0, -1, 1]
[0, 0, 1, 0, 0]
[1, -1, 0, 1, 0]
[0, 1, 0, 0, 1]

Vacuum moved to (0, 1)
Cleaned cell (0, 1)
[0, 0, 0, -1, 1]
[0, 0, 1, 0, 0]
[1, -1, 0, 1, 0]
[0, 1, 0, 0, 1]

Vacuum moved to (1, 1)
Vacuum moved to (1, 2)
Cleaned cell (1, 2)
[0, 0, 0, -1, 1]
[0, 0, 0, 0, 0]
[1, -1, 0, 1, 0]
[0, 1, 0, 0, 1]

Vacuum moved to (2, 2)
Vacuum moved to (2, 3)
Cleaned cell (2, 3)
[0, 0, 0, -1, 1]
[0, 0, 0, 0, 0]
[1, -1, 0, 0, 0]
[0, 1, 0, 0, 1]

Vacuum moved to (3, 3)
Vacuum moved to (3, 4)
Cleaned cell (3, 4)
[0, 0, 0, -1, 1]
[0, 0, 0, 0, 0]
[1, -1, 0, 0, 0]
[0, 1, 0, 0, 0]

Vacuum moved to (2, 4)
Vacuum moved to (1, 4)
Vacuum moved to (0, 4)
Cleaned cell (0, 4)
[0, 0, 0, -1, 0]
[0, 0, 0, 0, 0]
[1, -1, 0, 0, 0]
[0, 1, 0, 0, 0]

Vacuum moved to (1, 4)
Vacuum moved to (1, 3)
Vacuum moved to (1, 2)
Vacuum moved to (1, 1)
Vacuum moved to (1, 0)
Vacuum moved to (2, 0)
Cleaned cell (2, 0)
[0, 0, 0, -1, 0]
[0, 0, 0, 0, 0]
[0, -1, 0, 0, 0]
[0, 1, 0, 0, 0]

Vacuum moved to (3, 0)
Vacuum moved to (3, 1)
Cleaned cell (3, 1)
[0, 0, 0, -1, 0]
[0, 0, 0, 0, 0]
[0, -1, 0, 0, 0]
[0, 0, 0, 0, 0]

✅ All cells are clean!
Total movements: 18

