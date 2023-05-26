def make_change_greedy(coins, amount):
    """
    A function to find the minimum number of coins required to make change for a given amount using a greedy approach.
    :param coins: a list of denominations of coins available
    :param amount: the amount for which change is to be made
    :return: the minimum number of coins required to make change for the given amount
    """
    num_coins = 0
    coins.sort(reverse=True) # sort the coins in descending order
    
    for coin in coins:
        while amount >= coin:
            num_coins += 1
            amount -= coin
    
    return num_coins
