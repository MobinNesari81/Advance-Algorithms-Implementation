def rod_cutting(lengths, prices, n):
    # Initialize an array to store the maximum revenue for each length
    max_revenue = [0] * (n + 1)

    # Compute the maximum revenue for each length from 1 to n
    for i in range(1, n + 1):
        # Try all possible cuts of length j and compute the maximum revenue
        for j in range(1, i + 1):
            max_revenue[i] = max(max_revenue[i], prices[j - 1] + max_revenue[i - j])

    # Return the maximum revenue for length n
    return max_revenue[n]
