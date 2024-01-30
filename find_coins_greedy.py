def find_coins_greedy(amount):
    available_coin = [50, 25, 10, 5, 2, 1]
    coins_used = {}

    for coin in available_coin:
        if amount >= coin:
            num_coins = amount // coin
            coins_used[coin] = num_coins
            amount -= num_coins * coin

    return coins_used


if __name__ == "__main__":
    print(find_coins_greedy(113))
