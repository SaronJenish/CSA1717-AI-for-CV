import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        x, y = current_node.position
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for next_pos in neighbors:
            if (0 <= next_pos[0] < len(grid)) and (0 <= next_pos[1] < len(grid[0])):
                if grid[next_pos[0]][next_pos[1]] == 1 or next_pos in closed_set:
                    continue

                neighbor = Node(next_pos, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(next_pos, end)
                neighbor.f = neighbor.g + neighbor.h

                if any(open_node.position == neighbor.position and open_node.f <= neighbor.f for open_node in open_list):
                    continue

                heapq.heappush(open_list, neighbor)

    return None

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)

if path:
    print("Path found:")
    print(path)
else:
    print("No path found.")

