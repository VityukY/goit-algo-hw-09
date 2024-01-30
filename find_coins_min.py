def find_coins_min(amount):
    coin_values = [1, 2, 5, 10, 25, 50]
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0
    coins_used = {}

    for i in range(1, amount + 1):
        for coin in coin_values:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coins_used[i] = coin

    result = {}
    remaining_amount = amount

    while remaining_amount > 0:
        coin = coins_used[remaining_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        remaining_amount -= coin

    return result
