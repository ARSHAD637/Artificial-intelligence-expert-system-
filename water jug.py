from collections import deque

def water_jug_4_3_get_2():
    cap4, cap3, target = 4, 3, 2
    
    start = (0, 0)
    q = deque([start])
    parent = {start: None}              # backpointer for path
    action  = {start: "start"}          # action taken to reach state
    seen = {start}

    def neighbors(x, y):
        moves = []
        # Fill operations
        moves.append(((cap4, y), "Fill 4-gal"))
        moves.append(((x, cap3), "Fill 3-gal"))
        # Empty operations
        moves.append(((0, y), "Empty 4-gal"))
        moves.append(((x, 0), "Empty 3-gal"))
        # Pour 4 -> 3
        pour = min(x, cap3 - y)
        moves.append(((x - pour, y + pour), "Pour 4→3"))
        # Pour 3 -> 4
        pour = min(y, cap4 - x)
        moves.append(((x + pour, y - pour), "Pour 3→4"))
        return moves

    goal = None
    while q:
        x, y = q.popleft()
        if x == target: 
            goal = (x, y); break
        if y == target:
            # If asked to have the 2 gallons specifically in the 4-gallon jug,
            # continue; otherwise could stop here.
            pass
        for (nx, ny), act in neighbors(x, y):
            s = (nx, ny)
            if s not in seen:
                seen.add(s)
                parent[s] = (x, y)
                action[s] = act
                q.append(s)
                if nx == target: 
                    goal = s; q.clear(); break

    # Reconstruct path
    path = []
    cur = goal
    while cur is not None:
        path.append((cur, action[cur]))
        cur = parent[cur]
    path.reverse()
    return path

steps = water_jug_4_3_get_2()
for i, (state, act) in enumerate(steps):
    print(f"{i}: {state} via {act}")
