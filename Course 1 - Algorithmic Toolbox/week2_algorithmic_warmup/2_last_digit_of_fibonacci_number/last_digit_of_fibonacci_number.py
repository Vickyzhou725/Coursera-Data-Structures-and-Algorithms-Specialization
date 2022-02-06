# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    fibonacci_last_digit_list = list()
    fibonacci_last_digit_list.append(0)
    fibonacci_last_digit_list.append(1)

    for i in range(2, n+1):
        fibonacci_last_digit_list.append(
            (fibonacci_last_digit_list[i-1] + fibonacci_last_digit_list[i-2]) % 10
        )
    return fibonacci_last_digit_list[n]


def stress_test(N):
    for n in range(N+1):
        print(n)
        naive_result = last_digit_of_fibonacci_number_naive(n)
        fast_result = last_digit_of_fibonacci_number(n)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(40)
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
