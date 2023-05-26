def linear_time_median(arr):
    """
    Finds the median of a list in O(n) time using the divide and conquer approach.
    """
    n = len(arr)
    
    # Base case
    if n == 1:
        return arr[0]
    
    # Divide the list into sublists of size 5
    sublists = [arr[i:i+5] for i in range(0, n, 5)]
    
    # Find the median of each sublist using another algorithm (e.g. selection sort)
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    
    # Recursively find the median of the medians
    pivot = linear_time_median(medians)
    
    # Partition the list around the pivot
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    
    k = len(left)
    
    # Determine whether the pivot is the median or if we need to recurse on one side
    if k == n//2:
        return pivot
    elif k < n//2:
        return linear_time_median(right)
    else:
        return linear_time_median(left)
