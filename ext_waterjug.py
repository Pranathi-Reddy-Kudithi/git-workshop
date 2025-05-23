from collections import deque
import math

def minSteps(m, n, d):
    if d > max(m, n) or d % math.gcd(m, n) != 0:
        return "Can't obtain the required state"

    q = deque([(0, 0, 0)])
    visited = set([(0, 0)])
    prev_state = {}

    while q:
        jug1, jug2, steps = q.popleft()
        if jug1 == d or jug2 == d:
            path = []
            while (jug1, jug2) in prev_state:
                path.append((jug1, jug2))
                jug1, jug2 = prev_state[(jug1, jug2)]
            path.append((0, 0))
            path.reverse()

            print("Steps to reach the target state:")
            for state in path:
                print(state)
            return steps

        # List of possible actions
        actions = [
            (m, jug2),   # Fill jug1
            (jug1, n),   # Fill jug2
            (0, jug2),   # Empty jug1
            (jug1, 0),   # Empty jug2
            (jug1 - min(jug1, n - jug2), jug2 + min(jug1, n - jug2)),  # Pour jug1 → jug2
            (jug1 + min(jug2, m - jug1), jug2 - min(jug2, m - jug1))   # Pour jug2 → jug1
        ]

        for new_state in actions:
            if new_state not in visited:
                visited.add(new_state)
                q.append((*new_state, steps + 1))
                prev_state[new_state] = (jug1, jug2)  # Store parent state

    return "No solution found"

# Example Usage
print("Minimum steps:", minSteps(4, 3, 2))
