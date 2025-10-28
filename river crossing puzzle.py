# Missionaries and Cannibals Problem using BFS

from collections import deque

# Each state is represented as (M_left, C_left, Boat_side)
# Boat_side = 1 (left), 0 (right)
# Goal state: (0, 0, 0)

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set([start])
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # possible moves

    while queue:
        (m_left, c_left, boat), path = queue.popleft()
        if (m_left, c_left, boat) == goal:
            return path + [goal]

        for m, c in moves:
            if boat == 1:
                new_state = (m_left - m, c_left - c, 0)
            else:
                new_state = (m_left + m, c_left + c, 1)

            if is_valid(*new_state[:2]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(m_left, c_left, boat)]))
    return None

# Run BFS and print the path
solution = bfs()
print("Solution path:\n")
for state in solution:
    print(state)


output:
Solution path:

(3, 3, 1)
(3, 1, 0)
(3, 2, 1)
(3, 0, 0)
(3, 1, 1)
(1, 1, 0)
(2, 2, 1)
(0, 2, 0)
(0, 3, 1)
(0, 1, 0)
(1, 1, 1)
(0, 0, 0)

