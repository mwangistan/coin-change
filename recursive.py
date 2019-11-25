def min_change_rec(total, coins, memo=dict()):
    """Get minimum change using a recursive function
    """
    if total < 0:
        return 0
    if total == 0:
        return 1
    if total in memo.keys(): return memo[total]
    else:
        res = total + 1
        for i in range(len(coins)):
            coin = coins[i]
            if coin <= total:
                result = min_change_rec(total-coin, coins[i:], memo)
                if res > result + 1:
                    res = result + 1

        memo[total] = res
        return res
