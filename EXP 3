from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(f"Jug A: {a} liters, Jug B: {b} liters")

        if a == target or b == target:
            print("Reached the target!")
            return True

        next_states = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0),
            (min(a + b, capacity_a), b - (min(a + b, capacity_a) - a)),
            (a - (min(a + b, capacity_b) - b), min(a + b, capacity_b))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution found.")
    return False

water_jug_bfs(4, 3, 2)
