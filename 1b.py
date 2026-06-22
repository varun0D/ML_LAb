def objective_function(x):
    return -(x - 3) ** 2 + 9


def hill_climbing(start, step_size, max_iterations):
    current = start
    current_value = objective_function(current)

    for _ in range(max_iterations):

        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        if left_value > current_value:
            current = left
            current_value = left_value

        elif right_value > current_value:
            current = right
            current_value = right_value

        else:
            break

    return current, current_value


start = 0
step_size = 0.1
max_iterations = 100

best_solution, best_value = hill_climbing(
    start,
    step_size,
    max_iterations
)

print("Best Solution:", best_solution)
print("Maximum Value:", best_value)
