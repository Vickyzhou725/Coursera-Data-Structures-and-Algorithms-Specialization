# python3
import random

def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if b == 0:
        return a
    else:
        a_prim = a % b
        return gcd(b, a_prim)


def stress_test(lower, upper):
    while True:
        a, b = random.randint(lower, upper), random.randint(lower, upper)
        print(a, b)
        naive_result = gcd_naive(a, b)
        fast_result = gcd(a, b)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(1, 2 * 10 ** 6)
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
