import math

# Min-Max Function
def minimax(depth, nodeIndex, maximizingPlayer, values, maxDepth):

    # Leaf node reached
    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, maxDepth),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, maxDepth)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, maxDepth),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, maxDepth)
        )

# Leaf node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

# Tree depth
maxDepth = int(math.log2(len(values)))

# Execute Min-Max
result = minimax(0, 0, True, values, maxDepth)

print("Optimal value:", result)
