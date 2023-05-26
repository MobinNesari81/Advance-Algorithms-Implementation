# Scheduling to Minimizing Lateness Problem

The Scheduling to Minimizing Lateness problem is another classic optimization problem in computer science. The problem asks us to schedule jobs on a single machine such that the maximum lateness (i.e., the difference between the completion time of a job and its deadline) is minimized.

For example, if we have a list of four jobs:

```
[(1, 2, 4), (2, 3, 5), (3, 2, 6), (4, 1, 2)]
```

We need to determine the optimal schedule as well as the minimum lateness that can be obtained by scheduling these jobs on a single machine.

## Greedy Approach

One common approach to solving the Scheduling to Minimizing Lateness problem is the greedy approach. In this approach, we sort the jobs by their deadline in ascending order. We then loop through the sorted jobs and schedule them based on their processing times.

For each job, we update the current time and calculate the lateness of the job (i.e., the difference between its completion time and its deadline). We then update the maximum lateness if necessary. We continue this process until all jobs have been scheduled.

Note that the greedy approach may not always give us the optimal solution. However, the greedy approach is often efficient and works well for many instances of the Scheduling to Minimizing Lateness problem.

## Implementation

The implementation provided above uses a greedy approach to solve the Scheduling to Minimizing Lateness problem. The function `scheduling_lateness()` takes a list of jobs as input, where each job is represented as a tuple containing three integers: the job identifier, the processing time, and the deadline. The function returns the minimum lateness using the greedy approach.

We first sort the `jobs` list by their deadline in ascending order. We then loop through the sorted jobs and schedule them based on their processing times. For each job, we update the current time and calculate the lateness of the job (i.e., the difference between its completion time and its deadline). We then update the maximum lateness if necessary.

We continue this process until all jobs have been scheduled. Finally, we return the maximum lateness.

Here's an example usage of the `scheduling_lateness()` function:

```python
jobs = [(1, 2, 4), (2, 3, 5), (3, 2, 6), (4, 1, 2)]
min_lateness = scheduling_lateness(jobs)
print(min_lateness) # Output: 2
```

In this example, we have a list of four jobs. The function returns `2` as the minimum lateness using the greedy approach.