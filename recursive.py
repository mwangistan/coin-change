def min_change_rec(total, coins, memo=dict()):
    """Get minimum change using a recursive function
    """
    if total == 0:
        return 0
    if (total, len(coins)) in memo.keys(): return memo[(total, len(coins))]
    else:
        res = total + 1
        for i in range(len(coins)):
            coin = coins[i]
            if total >= coin:
                sub_res = min_change_rec(total-coin, coins[i:], memo)
                if sub_res + 1 < res:
                    res = sub_res + 1
        memo[(total, len(coins))] = res

    return res
