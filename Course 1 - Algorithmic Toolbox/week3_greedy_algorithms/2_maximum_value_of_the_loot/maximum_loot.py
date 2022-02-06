# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    value = 0
    n = len(weights)
    unit_weight_prices = [prices[i] / weights[i] for i in range(n)]
    index_map = {x[1]: x[0] for x in enumerate(unit_weight_prices)}
    unit_weight_prices.sort(reverse=True)
    for unit_price in unit_weight_prices:
        if capacity == 0:
            break
        else:
            index = index_map.pop(unit_price)
            add_weight = min(weights[index], capacity)
            add_value = add_weight * unit_price
            capacity -= add_weight
            value += add_value
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
