def min_coins(coins, amount):
    """
    Returns the min coins required to make change
    """ 
    rs = [amount+1 for m in range(amount+1)]
    rs[0] = 0
    for i in range(1, amount+1):
        for c in coins:
            if i >= c:
                rs[i] = min(rs[i], rs[i-c] + 1)

    if rs[amount] == amount+1:
        return -1
    return rs[amount]
