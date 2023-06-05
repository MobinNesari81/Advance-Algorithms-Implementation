# Knapsack Problem with Dynamic Programming

This is a Python implementation of the knapsack problem using dynamic programming. Given a set of items with weights and values, and a knapsack with a limited weight capacity, the goal is to maximize the total value of the items that can be placed into the knapsack.

## Dynamic Programming Approach

The key idea behind the dynamic programming approach to this problem is to break it down into smaller subproblems and store the results of those subproblems in an array. Specifically, we can define an array `max_values` such that `max_values[i][j]` represents the maximum value that can be obtained using a knapsack of capacity `j` and a subset of the first `i` items. We can then fill in this array iteratively, starting with `max_values[0][j] = 0` (since there are no items to choose from initially) and working our way up to `max_values[n][capacity]`, where `n` is the number of items.

To compute `max_values[i][j]`, we need to consider two cases: either we take the `i`-th item or we don't. If we don't take the `i`-th item, then the maximum value is simply the maximum value that can be obtained using a knapsack of capacity `j` and the first `i-1` items (`max_values[i-1][j]`). If we do take the `i`-th item, then the maximum value is the sum of its value and the maximum value that can be obtained using a knapsack of capacity `j - weight[i]` and the first `i-1` items (since we have used up `weight[i]` units of capacity).

Once we have filled in the `max_values` array, we can find the optimal set of items by working backwards from the end of the sequence. Specifically, we start at `max_values[n][capacity]` and check whether we took the `n`-th item (by comparing `max_values[n][capacity]` to `max_values[n-1][capacity]`). If we did, then we add it to the optimal set of items (which we will construct in reverse order). We continue this process for each item until we reach the beginning of the sequence or run out of capacity.

By computing the maximum achievable value and the optimal set of items using dynamic programming, we can solve the knapsack problem in O(nc) time, where `n` is the number of items and `c` is the weight capacity of the knapsack. This is much faster than the brute force approach of considering all possible subsets of items, which would take O(2^n) time.

## Usage

To use the `knapsack` function, simply provide three lists `weights`, `values`, and `capacity`. The `weights` and `values` lists should have the same length and correspond to the weights and values of each item, where `weights[i]` and `values[i]` represent the weight and value of item `i`. The `capacity` parameter represents the weight capacity of the knapsack. The function returns a tuple containing the optimal set of items (as a list of indices) and the maximum achievable value.

```python
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

optimal_items, optimal_value = knapsack(weights, values, capacity)
print("Optimal set of items:", optimal_items)
print("Optimal value:", optimal_value)
```

This will output the following result:

```
Optimal set of items: [1, 2]
Optimal value: 220
```

which means that the optimal set of items to put in the knapsack with a capacity of 50 units (given their weights and values `[10, 20, 30]` and `[60, 100, 120]`, respectively) is items 1 and 2 (with respective weights of 20 and 30 units), with a total value of 220 units.