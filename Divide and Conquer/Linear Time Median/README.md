# Linear Time Median Problem

The Linear Time Median problem is the problem of finding the median of a list in linear (O(n)) time. The median of a list is the middle element when the list is sorted. If the length of the list is even, the median is the average of the two middle elements.

Finding the median of a list is an important problem in statistics and has many practical applications. There are several algorithms for solving this problem, including the QuickSelect algorithm, the Median of Medians algorithm, and the Divide and Conquer approach.

In this implementation, we use the Divide and Conquer approach to solve the problem.

## Divide and Conquer Approach

The Divide and Conquer approach involves dividing a problem into smaller subproblems, solving each subproblem independently, and then combining the solutions to obtain the solution to the original problem. The algorithm works in three steps: divide, conquer, and combine.

1. **Divide**: We divide the list into sublists of size 5.
2. **Conquer**: For each sublist, we find the median using another algorithm (such as selection sort).
3. **Combine**: We recursively find the median of the medians obtained in step 2 until we have only one median left. We then partition the original list around this median and determine whether it is the median or if we need to recurse on one side.

The base case for the recursion is when the length of the list is 1. For small lists of length less than 5, we can simply compute the median using another algorithm, such as selection sort.

## Implementation

The implementation provided above uses a recursive function `linear_time_median()` to find the median of a list in O(n) time using the Divide and Conquer approach. The function takes a list as input and returns the median of the list.

To use this implementation, you can simply call the `linear_time_median()` function with a list as input:

```python
arr = [1, 5, 2, 6, 3, 7, 4, 8]
median = linear_time_median(arr)
print(median) # Output: 4
```

This will output the median of the input list, which is 4 in this example.

Note that for simplicity, this implementation assumes that the length of the input list is odd. If the length is even and you want to find the median of the two middle elements, you will need to make some modifications to the code.