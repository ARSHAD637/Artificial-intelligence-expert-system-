import numpy as np
import random

# Grid setup (5x5 example)
grid = np.zeros((5,5))
start = (0,0)
goal = (4,4)
obstacles = [(1,2), (3,2), (2,3)]
for x, y in obstacles:
    grid[x, y] = -1  # -1 for obstacle

actions = ['up', 'down', 'left', 'right']
action_idx = {a:i for i, a in enumerate(actions)}

def next_state(state, action):
    x, y = state
    if action == 'up' and x > 0:
        x -= 1
    elif action == 'down' and x < 4:
        x += 1
    elif action == 'left' and y > 0:
        y -= 1
    elif action == 'right' and y < 4:
        y += 1
    return (x, y)

def reward(state):
    if state == goal:
        return 10
    elif state in obstacles:
        return -10
    else:
        return -1

# Q-learning parameters
alpha = 0.7      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.2    # exploration rate
episodes = 500

# Q-table: rows for all possible states, cols for actions
Q = np.zeros((5,5,len(actions)))

for ep in range(episodes):
    state = start
    while state != goal:
        if random.uniform(0,1) < epsilon:
            act = random.choice(actions)
        else:
            act = actions[np.argmax(Q[state[0], state[1]])]
        next_s = next_state(state, act)
        r = reward(next_s)
        # Q update
        Q[state[0], state[1], action_idx[act]] = Q[state[0], state[1], action_idx[act]] + alpha * (r + gamma * np.max(Q[next_s[0], next_s[1]]) - Q[state[0], state[1], action_idx[act]])
        if next_s == goal or next_s in obstacles:
            break
        state = next_s

print("Learned Q-table:")
print(np.round(Q, 2))

# Recover optimal path
def get_optimal_path(Q, start, goal):
    state = start
    path = [state]
    while state != goal:
        a = actions[np.argmax(Q[state[0], state[1]])]
        state = next_state(state, a)
        path.append(state)
        if len(path) > 25:
            break
    return path

opt_path = get_optimal_path(Q, start, goal)
print("Optimal path from start to goal:", opt_path)
