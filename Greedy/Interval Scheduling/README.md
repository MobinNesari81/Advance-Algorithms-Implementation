# Interval Scheduling Problem

The interval scheduling problem is a classic optimization problem in computer science. The problem asks us to find the maximum number of non-overlapping intervals from a given list of intervals.

For example, if we have a list of eleven intervals:

```
[(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
```

We need to determine the maximum number of non-overlapping intervals that can be selected from this list.

## Greedy Approach

One common approach to solving the interval scheduling problem is the greedy approach. In this approach, we always pick the interval with the earliest end time and discard any overlapping intervals.

For example, let's say we have a list of four intervals:

```
[(1, 4), (3, 5), (0, 6), (5, 7)]
```

We begin by sorting the intervals by their end time, giving us the order `(1, 4), (3, 5), (5, 7), (0, 6)`.

We start by picking the interval with the earliest end time (`(1, 4)`) and discarding any overlapping intervals. Since the other two intervals overlap with this one, we discard them and move on to the next interval.

At this point, we have one non-overlapping interval (`(1, 4)`). We then pick the interval with the earliest end time among the remaining intervals (`(3, 5)`) and discard any overlapping intervals. Since there are no overlapping intervals, we add this interval to our list of non-overlapping intervals and move on to the next interval.

We continue this process, always picking the interval with the earliest end time among the remaining intervals and discarding any overlapping intervals. We continue until there are no more intervals left to consider.

Note that the greedy approach may not always give us the optimal solution. For example, if we have a list of three intervals:

```
[(0, 3), (1, 4), (2, 5)]
```

The greedy approach would give us a different set of non-overlapping intervals than the optimal solution (`(0, 3), (4, 5)` instead of `(1, 4), (4, 5)`). However, the greedy approach is often efficient and works well for many instances of the interval scheduling problem.

## Implementation

The implementation provided above uses a greedy approach to solve the interval scheduling problem. The function `interval_scheduling()` takes a list of intervals as input, where each interval is represented as a tuple containing two integers: the start time and the end time. The function returns the maximum number of non-overlapping intervals using the greedy approach.

We first sort the `intervals` list by their end time. We then loop through the intervals and count the non-overlapping ones by checking if the start time of each interval is greater than or equal to the current end time. If it is, we increment the `num_intervals` counter and update the current end time to the end time of the current interval.

We continue this process until all intervals have been processed. Finally, we return the `num_intervals` counter, which represents the maximum number of non-overlapping intervals.

Here's an example usage of the `interval_scheduling()` function:

```python
intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
max_intervals = interval_scheduling(intervals)
print(max_intervals) # Output: 4
```

In this example, we have a list of eleven intervals. The function returns `4`, which is the maximum number of non-overlapping intervals using the greedy approach.