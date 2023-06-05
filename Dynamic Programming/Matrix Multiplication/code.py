def matrix_chain_multiplication(p):
    # Initialize an array to store the minimum cost for each subchain
    n = len(p) - 1
    min_cost = [[0] * (n + 1) for _ in range(n + 1)]

    # Compute the minimum cost for each subchain from length 2 to n
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            min_cost[i][j] = float('inf')
            for k in range(i, j):
                cost = min_cost[i][k] + min_cost[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < min_cost[i][j]:
                    min_cost[i][j] = cost

    # Return the minimum cost and the optimal parenthesization
    return min_cost[1][n]

