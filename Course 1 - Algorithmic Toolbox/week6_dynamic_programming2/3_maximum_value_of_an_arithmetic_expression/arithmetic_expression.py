# python3
def calc(a, b, op):
    if op == '-':
        return a - b
    elif op == '+':
        return a + b
    elif op == '*':
        return a * b
    else:
        raise Exception ('operation not recognized!')


def min_and_max(i, j, m, M, digits, operations):
    min_val, max_val = float('inf'), float('-inf')
    for k in range(i, j):
        a = calc(M[i][k], M[k + 1][j], operations[k])
        b = calc(M[i][k], m[k + 1][j], operations[k])
        c = calc(m[i][k], M[k + 1][j], operations[k])
        d = calc(m[i][k], m[k + 1][j], operations[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    # i == j, expression only contains 1 number wo operations, min = max = di = dj
    digits, operations = dataset[::2], dataset[1::2]
    n = len(digits)
    m, M = [[0] * len(digits) for x in digits], [[0] * len(digits) for x in digits]
    for i in range(n):
        m[i][i], M[i][i] = int(digits[i]), int(digits[i])
    # for s from 1 to n-1, j = i + s, expression length = j-i
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, m, M, digits, operations)
    return M[0][-1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
