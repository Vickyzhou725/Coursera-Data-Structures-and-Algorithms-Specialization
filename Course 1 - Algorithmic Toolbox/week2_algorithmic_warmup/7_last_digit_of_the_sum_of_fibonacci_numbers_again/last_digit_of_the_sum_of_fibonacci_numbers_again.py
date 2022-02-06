# python3
import random


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


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


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    # S(n) = F(n+1) + F(n) - F(1) - F(0) = F(n+2) - 1
    # S(n) % 10 = F(n+2) - 1 % 10 = F(remainder) - 1 % 10 = last digit of remainder - 1
    from_remainder = fibonacci_number_remainder(from_index-1+2, 10)
    from_last_digit = last_digit_of_fibonacci_number(from_remainder) - 1
    to_remainder = fibonacci_number_remainder(to_index+2, 10)
    to_last_digit = last_digit_of_fibonacci_number(to_remainder) - 1

    last_digit = to_last_digit - from_last_digit
    return last_digit if last_digit >= 0 else last_digit + 10


def stress_test(N):
    while True:
        m, n = random.randint(0, N), random.randint(0, N)
        if m <= n:
            from_index, to_index = m, n
        else:
            from_index, to_index = n, m
        print(from_index, to_index)
        naive_result = last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index)
        fast_result = last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(100000)
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
