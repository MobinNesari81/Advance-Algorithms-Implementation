def knapsack(weights, values, capacity):
    # Initialize an array to store the maximum value for each subproblem
    n = len(weights)
    max_values = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill in the max_values array iteratively
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                max_values[i][j] = max_values[i - 1][j]
            else:
                max_values[i][j] = max(max_values[i - 1][j], values[i - 1] + max_values[i - 1][j - weights[i - 1]])

    # Find the optimal set of items and its value
    optimal_value = max_values[n][capacity]
    optimal_items = []
    j = capacity
    for i in range(n, 0, -1):
        if max_values[i][j] != max_values[i - 1][j]:
            optimal_items.append(i - 1)
            j -= weights[i - 1]
        if j == 0:
            break
    optimal_items.reverse()

    # Return the optimal set of items and its value
    return optimal_items, optimal_value
