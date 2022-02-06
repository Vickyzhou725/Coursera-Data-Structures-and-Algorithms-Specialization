# python3

from sys import stdin


def maximum_gold(capacity, weights, max_weights={}):
    assert 0 <= capacity <= 10 ** 4
    assert 0 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    # since there's no need to compute all possibilities of w <= capacity
    # choose the recursive + memoization method
    key = (capacity, tuple(weights))
    if (capacity == 0) or (len(weights) == 0):
        # no capacity or no gold
        max_weights[key] = 0
    if key in max_weights.keys():
        return max_weights.get(key)
    max_weight = 0
    for i in range(len(weights)):
        remaining_weights = weights[:i] + weights[i+1:]
        w_not_used = maximum_gold(capacity, remaining_weights, max_weights=max_weights)
        w_used = maximum_gold(capacity-weights[i], remaining_weights, max_weights=max_weights) + weights[i] if capacity >= weights[i] else 0
        max_weight = max(max_weight, w_not_used, w_used)
    max_weights[(capacity, tuple(weights))] = max_weight
    return max_weight


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
