# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    fibonacci_numbers = list()
    fibonacci_numbers.append(0)
    fibonacci_numbers.append(1)

    for i in range(2, n+1):
        fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
    return fibonacci_numbers[n]


def stress_test(N):
    for n in range(N+1):
        print(n)
        naive_result = fibonacci_number_naive(n)
        fast_result = fibonacci_number(n)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(45)
    input_n = int(input())
    print(fibonacci_number(input_n))
