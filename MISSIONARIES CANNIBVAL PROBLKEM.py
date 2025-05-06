from collections import deque

def is_valid(state):
    m_left, c_left, m_right, c_right, _ = state
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def get_successors(state):
    m_left, c_left, m_right, c_right, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []
    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c, 'right')
        else:
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c, 'left')
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def solve():
    initial_state = (3, 3, 0, 0, 'left')
    goal_state = (0, 0, 3, 3, 'right')
    queue = deque()
    queue.append((initial_state, [initial_state]))
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state == goal_state:
            for p in path:
                print(p)
            return

        for successor in get_successors(state):
            queue.append((successor, path + [successor]))

solve()
