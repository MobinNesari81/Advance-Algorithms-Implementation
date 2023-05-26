def interval_scheduling(intervals):
    """
    A function to find the maximum number of non-overlapping intervals using a greedy approach.
    :param intervals: a list of tuples where each tuple contains two integers (start time, end time)
    :return: the maximum number of non-overlapping intervals
    """
    num_intervals = 0 # counter for the number of non-overlapping intervals
    current_end_time = -1 # initialize current end time to a negative value
    
    # sort the intervals by their end time
    intervals.sort(key=lambda x: x[1])
    
    # loop through the intervals and count the non-overlapping ones
    for interval in intervals:
        start_time, end_time = interval
        if start_time >= current_end_time:
            num_intervals += 1
            current_end_time = end_time
            
    return num_intervals
