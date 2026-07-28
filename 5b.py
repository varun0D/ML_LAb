MAX = 1000
MIN = -1000

# Alpha-Beta Pruning
def alphabeta(depth, index, isMax, values, alpha, beta):

    # If leaf node, return value
    if depth == 3:
        return values[index]

    if isMax:
        best = MIN

        for i in range(2):
            best = max(best, alphabeta(depth + 1, index * 2 + i,
                                       False, values, alpha, beta))
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = MAX

        for i in range(2):
            best = min(best, alphabeta(depth + 1, index * 2 + i,
                                       True, values, alpha, beta))
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Find optimal value
result = alphabeta(0, 0, True, values, MIN, MAX)

print("Optimal Value =", result)
