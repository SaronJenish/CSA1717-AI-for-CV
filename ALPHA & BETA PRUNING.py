# Alpha-Beta Pruning Algorithm

def alpha_beta_pruning(node, depth, alpha, beta, maximizingPlayer, values, tree):
    if depth == 0 or node not in tree:
        return values[node]

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in tree[node]:
            eval = alpha_beta_pruning(child, depth-1, alpha, beta, False, values, tree)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for child in tree[node]:
            eval = alpha_beta_pruning(child, depth-1, alpha, beta, True, values, tree)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

# Example game tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

values = {
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}

result = alpha_beta_pruning('A', 3, float('-inf'), float('inf'), True, values, tree)
print("Best value:", result)
