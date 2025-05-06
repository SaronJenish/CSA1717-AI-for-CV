def minimax(depth, node_index, is_max, values, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, values, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, values, max_depth)
        )

values = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = 3

best_value = minimax(0, 0, True, values, max_depth)
print("The optimal value is:", best_value)

