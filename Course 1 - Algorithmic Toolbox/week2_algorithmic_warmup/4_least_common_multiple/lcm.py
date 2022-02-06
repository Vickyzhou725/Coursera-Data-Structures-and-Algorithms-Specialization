# python3
import random

def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def gcd(a, b):
    if b == 0:
        return a
    else:
        a_prim = a % b
        return gcd(b, a_prim)


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    d = gcd(a, b)
    return int(a * b / d)


def stress_test(lower, upper):
    while True:
        a, b = random.randint(lower, upper), random.randint(lower, upper)
        print(a, b)
        naive_result = lcm_naive(a, b)
        fast_result = lcm(a, b)
        if naive_result == fast_result:
            print("OK")
        else:
            print(f"Wrong Answer: {naive_result}, {fast_result}")
            return -1


if __name__ == '__main__':
    stress_test(1, 1000)
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
