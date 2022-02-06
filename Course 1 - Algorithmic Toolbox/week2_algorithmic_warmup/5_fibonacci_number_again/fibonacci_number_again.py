# python3
import random

def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


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


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    pisano_period = get_pisano_period(m)
    # F(n) % m = F(n') % m, where n' = n % len(pisano_period)
    n_prim = n % len(pisano_period)
    return fibonacci_number(n_prim) % m


def stress_test(N, M):
    while True:
        n, m = random.randint(1, N), random.randint(2, M)
        print(n, m)
        naive_result = fibonacci_number_again_naive(n, m)
        fast_result = fibonacci_number_again(n, m)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(1000000, 1000)
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
