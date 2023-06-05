# Matrix Chain Multiplication with Dynamic Programming

This is a Python implementation of the matrix chain multiplication problem using dynamic programming. Given a chain of matrices with dimensions `p[0] x p[1], p[1] x p[2], ..., p[n-1] x p[n]`, the goal is to find the optimal way to multiply the matrices such that the overall computational cost is minimized.

## Dynamic Programming Approach

The key idea behind the dynamic programming approach to this problem is to break it down into smaller subproblems and store the results of those subproblems in an array. Specifically, we can define an array `min_cost` such that `min_cost[i][j]` represents the minimum computational cost of multiplying the subchain of matrices from `i` to `j` (inclusive). We can then fill in this array iteratively, starting with subchains of length 2 and working our way up to the full chain (`min_cost[1][n]`).

To compute `min_cost[i][j]`, we need to consider all possible ways of splitting the subchain into two subchains (one from `i` to `k` and one from `k+1` to `j`, where `i <= k < j`). For each of these splits, we can compute the total cost as the sum of the costs of multiplying the two subchains (which are stored in `min_cost[i][k]` and `min_cost[k+1][j]`) plus the cost of multiplying the resulting intermediate matrices (`p[i-1] x p[k] x p[j]`). We then take the minimum of these values as the value of `min_cost[i][j]`.

By computing the minimum cost for each subchain of the matrix chain in this way, we can solve the matrix chain multiplication problem in O(n^3) time, which is much faster than the brute force approach of considering all possible ways of parenthesizing the matrices.

## Usage

To use the `matrix_chain_multiplication` function, simply provide a list `p` containing the dimensions of the matrices in the chain (where `p[i]` represents the number of rows in matrix `i` and the number of columns in matrix `i+1`). The function returns the minimum computational cost of multiplying the chain of matrices using the optimal parenthesization.

```python
p = [5, 10, 3, 12, 5, 50, 6]
min_cost = matrix_chain_multiplication(p)
print("Minimum computational cost:", min_cost)
```

This will output the following result:

```
Minimum computational cost: 2010
```

which means that the minimum computational cost of multiplying the chain of matrices with dimensions `[5x10, 10x3, 3x12, 12x5, 5x50, 50x6]` using the optimal parenthesization is 2010.