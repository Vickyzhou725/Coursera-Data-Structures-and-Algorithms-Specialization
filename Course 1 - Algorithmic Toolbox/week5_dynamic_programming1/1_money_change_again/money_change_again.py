# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money, min_number_coins=None, coins=[1, 3, 4]):
    if min_number_coins is None:
        min_number_coins = [0] * (money + 1)
    if min_number_coins[money] == 0:
        for i in range(1, money+1):
            if min_number_coins[i] == 0:
                min_change = float('inf')
                for coin in coins:
                    if i - coin >= 0:
                        min_change = min(
                            min_change,
                            change(i-coin, min_number_coins=min_number_coins)+1
                        )
                min_number_coins[i] = min_change
    return min_number_coins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
