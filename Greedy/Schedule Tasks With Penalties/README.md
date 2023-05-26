# Scheduling Tasks with Deadlines and Penalties for a Single Processor Problem

The Scheduling Tasks with Deadlines and Penalties for a Single Processor problem is a classic optimization problem in computer science. The problem asks us to determine the maximum profit that can be obtained by scheduling tasks with deadlines and penalties on a single processor.

For example, if we have a list of four tasks:

```
[(1, 2, 10), (2, 1, 5), (3, 2, 1), (4, 1, 3)]
```

We need to determine the optimal schedule as well as the maximum profit that can be obtained by scheduling these tasks on a single processor.

## Greedy Approach

One common approach to solving the Scheduling Tasks with Deadlines and Penalties for a Single Processor problem is the greedy approach. In this approach, we sort the tasks by their penalty in descending order. We then loop through the sorted tasks and schedule them based on their deadlines.

For each task, we find the latest available slot for that task (i.e., the latest slot before its deadline that is not yet taken). If such a slot exists, we schedule the task and update the scheduled list and the schedule. We continue this process until all tasks have been scheduled.

Note that the greedy approach may not always give us the optimal solution. However, the greedy approach is often efficient and works well for many instances of the Scheduling Tasks with Deadlines and Penalties for a Single Processor problem.

## Implementation

The implementation provided above uses a greedy approach to solve the Scheduling Tasks with Deadlines and Penalties for a Single Processor problem. The function `scheduling_tasks()` takes a list of tasks as input, where each task is represented as a tuple containing three integers: the task identifier, the deadline, and the penalty for missing the deadline. The function returns a list of task identifiers representing the optimal schedule as well as the maximum profit using the greedy approach.

We first sort the `tasks` list by their penalty in descending order. We then loop through the sorted tasks and schedule them based on their deadlines. For each task, we find the latest available slot for that task (i.e., the latest slot before its deadline that is not yet taken). If such a slot exists, we schedule the task and update the scheduled list and the schedule.

We continue this process until all tasks have been scheduled. Finally, we calculate the total profit by summing the penalties of all scheduled tasks.

Here's an example usage of the `scheduling_tasks()` function:

```python
tasks = [(1, 2, 10), (2, 1, 5), (3, 2, 1), (4, 1, 3)]
schedule, profit = scheduling_tasks(tasks)
print(schedule) # Output: [1, 3, 0, 0]
print(profit) # Output: 11
```

In this example, we have a list of four tasks. The function returns `[1, 3, 0, 0]` as the optimal schedule, where `0` represents an unscheduled task, and `11` as the maximum profit using the greedy approach.