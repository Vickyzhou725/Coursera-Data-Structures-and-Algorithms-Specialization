# python3


def compute_operations(n, operations=['*3', '*2', '+1'],
                       min_operations=None,
                       min_number_operations=None):
    # assert 1 <= n <= 10 ** 6
    if min_number_operations is None:
        min_number_operations = [0] * (n+1)
    if min_operations is None:
        min_operations = [[]] * (n+1)
    if min_number_operations[n] == 0:
        for i in range(2, n+1):
            if min_number_operations[i] == 0:
                min_num_op = float('inf')
                min_op = []
                for operation in operations:
                    if (operation[0] == '*') and (n % float(operation[1:]) == 0):
                        k = int(n / float(operation[1:]))
                        num_op, op = compute_operations(
                            k, min_operations=min_operations,
                            min_number_operations=min_number_operations
                        )
                        if (num_op + 1) < min_num_op:
                            min_num_op = num_op + 1
                            min_op = op
                    elif (operation[0] == '+') and (n-float(operation[1:]) >= 1):
                        k = int(n - float(operation[1:]))
                        num_op, op = compute_operations(
                            k, min_operations=min_operations,
                            min_number_operations=min_number_operations,
                        )
                        if (num_op + 1) < min_num_op:
                            min_num_op = num_op + 1
                            min_op = op
                min_number_operations[i] = min_num_op
                min_operations[i] = min_op
    return min_number_operations[n], min_operations[n] + [n]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    # print(len(output_sequence) - 1)
    print(output_sequence[0])
    print(*output_sequence[1], end=' ')
