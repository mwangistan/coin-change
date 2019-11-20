def num_coins(cents):
    '''Return the number of coins
    '''
    if cents < 1:
        return 0
    coins = [25, 10, 5, 1]
    num_coins = 0
    for coin in coins:
        num_coins += cents // coin
        cents = cents % coin
        if cents == 0:
            break
    return num_coins