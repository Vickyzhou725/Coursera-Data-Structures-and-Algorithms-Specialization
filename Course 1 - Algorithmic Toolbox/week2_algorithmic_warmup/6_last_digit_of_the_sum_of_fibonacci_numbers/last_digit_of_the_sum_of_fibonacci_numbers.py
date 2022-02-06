# python3
import random


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def fibonacci_number(n):
    fibonacci_numbers = list()
    fibonacci_numbers.append(0)
    fibonacci_numbers.append(1)

    for i in range(2, n+1):
        fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
    return fibonacci_numbers[n]


def get_pisano_period(m):
    pisano_period = list()
    pisano_period.append(0)
    i = 1
    while pisano_period[:int(len(pisano_period)/2)] != pisano_period[int(len(pisano_period)/2):]:
        pisano_period.append(fibonacci_number(i) % m)
        i += 1
    return pisano_period[:int(len(pisano_period)/2)]


def fibonacci_number_remainder(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    pisano_period = get_pisano_period(m)
    # F(n) % m = F(n') % m, where n' = n % len(pisano_period)
    n_prim = n % len(pisano_period)
    return n_prim


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 18

    fibonacci_last_digit_list = list()
    fibonacci_last_digit_list.append(0)
    fibonacci_last_digit_list.append(1)

    for i in range(2, n+1):
        fibonacci_last_digit_list.append(
            (fibonacci_last_digit_list[i-1] + fibonacci_last_digit_list[i-2]) % 10
        )
    return fibonacci_last_digit_list[n]


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    # S(n) = F(n+1) + F(n) - F(1) - F(0) = F(n+2) - 1
    # S(n) % 10 = F(n+2) - 1 % 10 = F(remainder) - 1 % 10 = last digit of remainder - 1
    remainder = fibonacci_number_remainder(n+2, 10)
    last_digit = last_digit_of_fibonacci_number(remainder) - 1
    return last_digit if last_digit >= 0 else last_digit + 10


def stress_test(N):
    while True:
        n = random.randint(0, N)
        print(n)
        naive_result = last_digit_of_the_sum_of_fibonacci_numbers_naive(n)
        fast_result = last_digit_of_the_sum_of_fibonacci_numbers(n)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(100000)
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))