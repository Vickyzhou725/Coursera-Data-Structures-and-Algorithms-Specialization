# python3
import random
from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def bubble_sort_descending(array):
    # O(n^2)
    # find the max value in the array[i:]
    # and put it to the ith position
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def max_dot_product(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(-10 ** 5 <= f <= 10 ** 5 for f in first_sequence)
    assert all(-10 ** 5 <= s <= 10 ** 5 for s in second_sequence)

    sorted_first_sequence = bubble_sort_descending(first_sequence)
    sorted_second_sequence = bubble_sort_descending(second_sequence)
    max_revenue = 0
    for x, y in zip(sorted_first_sequence, sorted_second_sequence):
        max_revenue += x * y
    return max_revenue


def stress_test(N, M):
    while True:
        n = random.randint(1, N)
        first_sequence, second_sequence = list(), list()
        for i in range(n):
            first_sequence.append(random.randint(0, M))
            second_sequence.append(random.randint(0, M))
        print(first_sequence, '\n', second_sequence)
        naive_result = max_dot_product_naive(first_sequence, second_sequence)
        fast_result = max_dot_product(first_sequence, second_sequence)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(10, 1000)
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
