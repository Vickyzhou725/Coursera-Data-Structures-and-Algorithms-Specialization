# python3
from math import sqrt, floor

def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    k = floor((sqrt(8*n+1)-1)/2)
    total = 0
    for i in range(1, k+1):
        summands.append(i)
        total += i
    # according to math, 0 <= n - total <= k+1
    # thus add the remainder to the first prize
    summands[-1] += n - total

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
