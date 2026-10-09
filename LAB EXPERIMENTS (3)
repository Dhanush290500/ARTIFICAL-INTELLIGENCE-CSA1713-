from collections import deque
import math


def water_jug_problem(jug1_cap, jug2_cap, target):
    # Check if a solution is mathematically possible.
    if target < 0 or target > max(jug1_cap, jug2_cap):
        return "No solution is possible."
    if target == 0:
        return [(0, 0)]
    if math.gcd(jug1_cap, jug2_cap) == 0 or target % math.gcd(jug1_cap, jug2_cap) != 0:
        return "No solution is possible."

    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        j1, j2, path = queue.popleft()

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        current_path = path + [(j1, j2)]
        if j1 == target or j2 == target:
            return current_path

        pour_1_to_2 = min(j1, jug2_cap - j2)
        pour_2_to_1 = min(j2, jug1_cap - j1)
        next_states = [
            (jug1_cap, j2),
            (j1, jug2_cap),
            (0, j2),
            (j1, 0),
            (j1 - pour_1_to_2, j2 + pour_1_to_2),
            (j1 + pour_2_to_1, j2 - pour_2_to_1),
        ]

        for state in next_states:
            queue.append((state[0], state[1], current_path))

    return "No solution is possible."


if __name__ == "__main__":
    print(water_jug_problem(4, 3, 2))
