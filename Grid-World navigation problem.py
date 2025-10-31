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



output:
Learned Q-table:
[[[ -1.39  -0.43  -1.39  -2.25]
  [ -3.98  -2.25  -1.39  -3.55]
  [ -3.44  -9.73  -2.38  -3.36]
  [ -3.04  -2.97  -2.74  -2.99]
  [ -2.54  -0.8   -2.51  -2.52]]

 [[ -1.39   0.63  -0.43   0.63]
  [ -4.     1.81  -0.43  -9.73]
  [  0.     0.     0.     0.  ]
  [ -2.67  -7.    -7.     0.75]
  [ -2.32   4.89  -1.96  -2.39]]

 [[ -0.43   1.81   0.63   1.81]
  [ -1.57   3.12   0.63   0.58]
  [ -9.73  -7.     1.81  -7.  ]
  [  0.     0.     0.     0.  ]
  [ -2.17   7.72  -9.1    1.06]]

 [[  0.63   3.12   1.81   3.12]
  [  1.81   4.58   1.81 -10.  ]
  [  0.     0.     0.     0.  ]
  [ -7.     8.     0.     7.27]
  [ -0.7   10.     0.     0.  ]]

 [[  1.78   2.98   2.61   4.58]
  [  3.12   4.58   3.12   6.2 ]
  [-10.     6.2    4.58   8.  ]
  [  6.2    8.     6.2   10.  ]
  [  0.     0.     0.     0.  ]]]
Optimal path from start to goal: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]
