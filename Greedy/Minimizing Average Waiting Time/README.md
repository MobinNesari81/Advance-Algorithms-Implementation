# Minimizing Average Waiting Time Problem

The minimizing average waiting time problem is a classic scheduling problem in computer science. The problem asks us to schedule a list of jobs with given arrival times and processing times in such a way that the average waiting time of all jobs is minimized.

For example, if we have a list of three jobs with arrival times `[0, 1, 2]` and processing times `[3, 9, 6]`, we need to determine the order in which these jobs should be processed so that the average waiting time is minimized.

## Greedy Approach

One common approach to solving the minimizing average waiting time problem is the greedy approach. In this approach, we always pick the job with the shortest processing time that has arrived by the current time.

For example, let's say we have a list of three jobs with arrival times `[0, 1, 2]` and processing times `[3, 9, 6]`. We begin by sorting the jobs by their arrival time, giving us the order `(0, 3), (1, 9), (2, 6)`.

We start at time `0` and check which jobs have arrived by this time. Since the first job has arrived, we add it to our list of jobs to be processed and set the current time to `3`.

At time `3`, we check which jobs have arrived by this time and find that the other two jobs have also arrived. We then pick the job with the shortest processing time (the first job) and process it until its completion time (`6`). We then set the current time to `6` and record the total wait time of this job as `3` since it arrived at time `0` and waited for `3` time units before being processed.

We continue this process, picking the job with the shortest processing time that has arrived by the current time and updating the current time and total wait time of each job accordingly. We continue until all jobs have been processed.

Note that the greedy approach may not always give us the optimal solution. For example, if we have a list of three jobs with arrival times `[0, 1, 2]` and processing times `[9, 3, 6]`, the greedy approach would give us a different order of processing the jobs than the optimal solution (`(0, 9), (2, 3), (1, 6)`). However, the greedy approach is often efficient and works well for many instances of the minimizing average waiting time problem.

## Implementation

The implementation provided above uses a greedy approach to solve the minimizing average waiting time problem. The function `minimize_avg_waiting_time()` takes a list of jobs as input, where each job is represented as a tuple containing two integers: the arrival time and the processing time. The function returns the minimum average waiting time for the given list of jobs using the greedy approach.

We first sort the `jobs` list by their arrival time. We then loop until all jobs are completed, adding all jobs that have arrived by the current time to a min-heap sorted by their processing time and popping the job with the shortest processing time from the heap at each step.

If there are no jobs in the heap but there are still jobs that have not arrived yet, we jump to the next arrival time. We continue this process until all jobs have been processed.

Finally, we return the total wait time divided by the number of jobs to get the minimum average waiting time.

Here's an example usage of the `minimize_avg_waiting_time()` function:

```python
jobs = [(0, 3), (1, 9), (2, 6)]
min_avg_wait_time = minimize_avg_waiting_time(jobs)
print(min_avg_wait_time) # Output: 9
```

In this example, we have a list of three jobs with arrival times `[0, 1, 2]` and processing times `[3, 9, 6]`. The function returns `9`, which is the minimum average waiting time for these jobs using the greedy approach.