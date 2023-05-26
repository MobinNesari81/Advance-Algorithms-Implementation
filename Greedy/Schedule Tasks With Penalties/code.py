def scheduling_tasks(tasks):
    """
    A function to find the maximum profit that can be obtained by scheduling tasks with deadlines and penalties
    on a single processor using a greedy approach.
    :param tasks: a list of tuples where each tuple contains three integers (task identifier, deadline, penalty)
    :return: a list of task identifiers representing the optimal schedule as well as the maximum profit
    """
    # sort the tasks by their penalty in descending order
    tasks.sort(key=lambda x: x[2], reverse=True)
    
    # initialize a boolean list of scheduled tasks and an integer list of the schedule
    scheduled = [False] * (len(tasks) + 1)
    schedule = [0] * len(tasks)
    
    # loop through the sorted tasks and schedule them based on their deadlines
    for i in range(len(tasks)):
        task_id, deadline, penalty = tasks[i]
        
        # find the latest available slot for the current task
        j = min(deadline, len(tasks)) - 1
        while j >= 0 and scheduled[j]:
            j -= 1
            
        # if there is a slot available, schedule the task and update the scheduled list and the schedule
        if j >= 0:
            scheduled[j] = True
            schedule[j] = task_id
    
    # calculate the total profit
    total_profit = sum([tasks[schedule[i]-1][2] for i in range(len(schedule)) if scheduled[i]])
    
    return schedule, total_profit
