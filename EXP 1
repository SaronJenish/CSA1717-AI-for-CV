
import heapq

GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def to_tuple(p): return tuple(num for row in p for num in row)

def heuristic(s):
    d = 0
    for i in range(3):
        for j in range(3):
            v = s[i][j]
            if v != 0:
                gx, gy = divmod(v - 1, 3)
                d += abs(i - gx) + abs(j - gy)
    return d

def find_zero(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i, j

def neighbors(s):
    x, y = find_zero(s)
    result = []
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [r[:] for r in s]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            result.append(new)
    return result

def solve(start):
    heap = []
    heapq.heappush(heap, (heuristic(start), 0, start, []))
    visited = set()

    while heap:
        est, cost, state, path = heapq.heappop(heap)
        t = to_tuple(state)
        if t in visited:
            continue
        visited.add(t)

        if state == GOAL:
            return path + [state]

        for n in neighbors(state):
            if to_tuple(n) not in visited:
                heapq.heappush(heap, (cost + 1 + heuristic(n), cost + 1, n, path + [state]))

    return None

def print_puzzle(p):
    for row in p:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()

if __name__ == "__main__":
    start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    result = solve(start)
    if result:
        for step in result:
            print_puzzle(step)
    else:
        print("No solution found.")
