# Map Coloring using CSP (Backtracking)

colors = ['Red', 'Green', 'Blue']

regions = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

def is_valid(region, color, assignment):
    for neighbor in regions[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

solution = backtrack({})
print("Solution:" if solution else "No solution found.")
print(solution)
