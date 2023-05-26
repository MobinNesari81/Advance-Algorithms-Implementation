def fractional_knapsack(items, capacity):
    """
    A function to find the maximum total value that can be obtained by putting items into a knapsack
    with a given capacity using a greedy approach.
    :param items: a list of tuples where each tuple contains two integers (value, weight) representing an item
    :param capacity: an integer representing the capacity of the knapsack
    :return: the maximum total value that can be obtained
    """
    # sort the items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    # initialize the total value and the current capacity of the knapsack
    total_value = 0
    curr_capacity = capacity
    
    # loop through the sorted items and add them to the knapsack if there is enough space
    for i in range(len(items)):
        value, weight = items[i]
        
        # if there is enough space, add the entire item to the knapsack
        if weight <= curr_capacity:
            total_value += value
            curr_capacity -= weight
        # otherwise, add a fraction of the item to the knapsack
        else:
            fraction = curr_capacity / weight
            total_value += fraction * value
            break
    
    return total_value
