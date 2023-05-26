## Description
Given an array of integers, the maximum-subarray problem is to find a contiguous subarray with the largest sum.

The divide and conquer approach involves recursively dividing the input array into halves until the base case is reached (i.e., the subproblem consists of a single element). Then, each subproblem's solution is combined to give the final output. 

To solve the maximum subarray problem using the divide and conquer approach, we can split the input array into two halves and compute the maximum subarray sum in each half separately. The maximum subarray sum that crosses the midpoint of the input array needs to be computed as well. Finally, the result can be calculated by returning the maximum of these three values.

## Example
Consider the following array of integers: [-2, 1, -3, 4, -1, 2, 1, -5, 4].

1. Divide the array into two halves: [-2, 1, -3, 4] and [-1, 2, 1, -5, 4].
2. Recursively compute the maximum subarray sum in each half.
    - Left half: max subarray sum is 4 (from index 3 to index 3).
    - Right half: max subarray sum is 6 (from index 1 to index 4).
3. Compute the maximum subarray sum that crosses the midpoint of the input array.
    - Max subarray sum crossing the midpoint is 7 (from index 3 to index 7).
4. Return the maximum of the three values computed in steps 2 and 3, which is 7.

## Usage
To use this code, simply call the `max_subarray` function and pass your array as an argument. The function returns the maximum subarray sum.

```python
my_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(my_array)) # output: 6
```
