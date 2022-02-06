# python3
import math


def money_change(money, coins=[10, 5, 1]):
    assert 0 <= money <= 10 ** 3
    change = 0
    for coin in coins:
        change += math.floor(money/coin)
        money %= coin
    if money != 0:
        print("Can't make the change!")
        return -1
    else:
        return change


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
