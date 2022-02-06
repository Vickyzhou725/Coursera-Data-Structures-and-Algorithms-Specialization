# python3
import random


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def find_max_number(numbers, n):
    index = 0
    for i in range(1, n):
        if numbers[i] > numbers[index]:
            index = i
    max = numbers[index]
    numbers[index] = numbers[n-1]
    numbers[n-1] = max

    return numbers


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    n = len(numbers)

    numbers = find_max_number(numbers, n)
    numbers = find_max_number(numbers, n-1)

    return numbers[n-1] * numbers[n-2]


def stress_test(N, M):
    while True:
        n = random.randint(2, N)
        numbers = list()
        for i in range(n):
            numbers.append(random.randint(0, M))
        print(numbers)
        naive_result = max_pairwise_product_naive(numbers)
        fast_result = max_pairwise_product(numbers)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(10, 100000)
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
