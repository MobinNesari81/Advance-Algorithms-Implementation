# Fractional Knapsack Problem

The Fractional Knapsack problem is a classic optimization problem in computer science. The problem asks us to determine the maximum total value that can be obtained by putting items into a knapsack with a given capacity.

For example, if we have a list of three items with their corresponding values and weights:

```
[(60, 10), (100, 20), (120, 30)]
```

And a knapsack with a capacity of `50`, we need to determine the optimal combination of items to put into the knapsack such that the maximum total value is achieved.

## Greedy Approach

One common approach to solving the Fractional Knapsack problem is the greedy approach. In this approach, we sort the items by their value-to-weight ratio in descending order. We then loop through the sorted items and add them to the knapsack if there is enough space.

For each item, we check if there is enough space to add the entire item to the knapsack. If there is, we add the entire item and update the total value and the current capacity of the knapsack. Otherwise, we add a fraction of the item to the knapsack and break out of the loop.

Note that the greedy approach may not always give us the optimal solution. However, the greedy approach is often efficient and works well for many instances of the Fractional Knapsack problem.

## Implementation

The implementation provided above uses a greedy approach to solve the Fractional Knapsack problem. The function `fractional_knapsack()` takes a list of items as input, where each item is represented as a tuple containing two integers: the value and the weight of the item. The function also takes an integer representing the capacity of the knapsack. The function returns the maximum total value that can be obtained using the greedy approach.

We first sort the `items` list by their value-to-weight ratio in descending order. We then loop through the sorted items and add them to the knapsack if there is enough space. For each item, we check if there is enough space to add the entire item to the knapsack. If there is, we add the entire item and update the total value and the current capacity of the knapsack. Otherwise, we add a fraction of the item to the knapsack and break out of the loop.

We continue this process until we have added all possible items to the knapsack or there is no more space left in the knapsack. Finally, we return the total value of the items in the knapsack.

Here's an example usage of the `fractional_knapsack()` function:

```python
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
max_value = fractional_knapsack(items, capacity)
print(max_value) # Output: 240.0
```

In this example, we have a list of three items with their corresponding values and weights. We also have a knapsack with a capacity of `50`. The function returns `240.0` as the maximum total value that can be obtained using the greedy approach.