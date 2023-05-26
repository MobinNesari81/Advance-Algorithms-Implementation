# Coin Changing Problem

The coin changing problem is a classic problem in computer science and mathematics. The problem asks us to find the minimum number of coins required to make change for a given amount using a set of available coin denominations.

For example, if we have coins with denominations `[25, 10, 5, 1]` and we need to make change for `63` cents, we can use two quarters (`25 + 25`), one dime (`10`), and three pennies (`1 + 1 + 1`) to make change for `63` cents.

## Greedy Approach

One common approach to solving the coin changing problem is the greedy approach. In this approach, we always pick the largest possible coin denomination at each step until we reach the target amount.

For example, let's say we have coins with denominations `[25, 10, 5, 1]` and we need to make change for `63` cents. Using the greedy approach, we would first pick a quarter (`25`) since it is the largest possible coin denomination that is less than or equal to `63`. We then subtract `25` from `63`, leaving us with `38` cents. We repeat this process, picking a quarter again since it is the largest possible coin denomination that is less than or equal to `38`. We have now used `50` cents worth of coins (`25 + 25`) and have `13` cents left to make change for.

We continue this process, picking a dime (`10`) since it is the largest possible coin denomination that is less than or equal to `13`. We have now used `60` cents worth of coins (`25 + 25 + 10`) and have `3` cents left to make change for.

Finally, we pick three pennies (`1 + 1 + 1`) since they are the largest possible coin denominations that are less than or equal to `3`. We have now used `63` cents worth of coins in total, which is the minimum number of coins required to make change for `63` cents.

Note that the greedy approach may not always give us the optimal solution. For example, if we have coins with denominations `[10, 6, 1]` and we need to make change for `12` cents, the greedy approach would give us four coins (`10 + 1 + 1 + 1`), while the optimal solution would be two coins (`6 + 6`). However, the greedy approach is often efficient and works well for many sets of coin denominations.

## Implementation

The implementation provided above uses a greedy approach to solve the coin changing problem. The function `make_change_greedy()` takes a list of coin denominations `coins` and an amount `amount` as input, and returns the minimum number of coins required to make change for the given amount using the greedy approach.

We begin by sorting the `coins` list in descending order, so that we can pick the largest possible coin denomination at each step. We then iterate through the `coins` list and check if `amount` is greater than or equal to the current coin denomination. If it is, we subtract the coin denomination from `amount` and increment the `num_coins` counter.

We continue this process until `amount` becomes zero, at which point we have found the minimum number of coins required to make change for the given amount using the greedy approach.

Here's an example usage of the `make_change_greedy()` function:

```python
coins = [25, 10, 5, 1]
amount = 63
num_coins = make_change_greedy(coins, amount)
print(num_coins) # Output: 6
```

In this example, we have `coins` list with denominations `[25, 10, 5, 1]` and `amount` equal to `63`. The function returns `6`, which is the minimum number of coins required to make change for `63` cents using the greedy approach.