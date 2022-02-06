# python3

from itertools import product
from sys import stdin

def match_value(target, values, results=dict()):
    key = (target, tuple(values))
    if target < 0:
        return -1
    if (target == 0) and (len(values) == 0):
        return []
    elif (target != 0) and (len(values) == 0):
        return -1
    elif (target == 0) and (len(values) != 0):
        return -1

    # if len(values) == 1:
    #     if target == values[0]:
    #         results[key] = [values[0]]
    #     else:
    #         results[key] = -1
    if key in results.keys():
        return results[key]

    for val in values:
        rslt = match_value(target-val, values, results=results)
        if rslt != -1:
            results[key] = rslt + [val]




def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    if len(values) < 3:
        return 0
    if sum(values) % 3 != 0:
        return 0
    partition_value = sum(values) // 3


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
