# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    # row:first sequence, col: second sequence
    n_row, n_col = len(first_sequence), len(second_sequence)
    dp_matrix = [[x for x in range(n_col+1)]] + [[x] + [-1] * (n_col) for x in range(1, n_row+1)]
    for i in range(1, n_row+1):
        for j in range(1, n_col+1):
            insertion = dp_matrix[i-1][j] + 1
            deletion = dp_matrix[i][j-1] + 1
            if first_sequence[i-1] == second_sequence[j-1]:
                match = dp_matrix[i-1][j-1]
            else:
                match = dp_matrix[i-1][j-1] + 2
            dp_matrix[i][j] = min(insertion, deletion, match)
    # total_elements = 2 * match + 2 * mismatch + 1 * insertion + 1 * deletion
    # edit_distance = 0 * match + 2 * mismatch + 1 * insertion + 1 * deletion
    # for i in dp_matrix:
    #     print(*i, sep='\t')
    return (n_row + n_col - dp_matrix[-1][-1]) // 2

#
# def get_alignment_cost(i, j, dp_matrix):
#     if (i == 0) and (j == 0):
#         return 0
#     # total_elements = 2 * match + 2 * mismatch + 1 * insertion + 1 * deletion
#     # edit_distance = 0 * match + 2 * mismatch + 1 * insertion + 1 * deletion
#     # alignment_cost = 0 * match + 2 * mismatch + 1 * insertion + 1 * deletion
#     if (i >= 1) and (j >= 1) and (dp_matrix[i][j] == dp_matrix[i-1][j-1]):    # 0 * match
#         alignment_cost = get_alignment_cost(i-1, j-1, dp_matrix)
#     elif (i >= 1) and (j >= 1) and (dp_matrix[i][j] == dp_matrix[i-1][j-1] + 2):    # 2 * mismatch
#         alignment_cost = get_alignment_cost(i-1, j-1, dp_matrix) + 2
#     elif (i >= 1) and (dp_matrix[i][j] == dp_matrix[i-1][j] + 1):  # 1 * insertion
#         alignment_cost = get_alignment_cost(i-1, j, dp_matrix) + 1
#     elif (j >= 1) and (dp_matrix[i][j] == dp_matrix[i][j-1] + 1):  # 1 * deletion
#         alignment_cost = get_alignment_cost(i, j-1, dp_matrix) + 1
#     else:
#         return -1
#     return alignment_cost
#
#
# def lcs2(first_sequence, second_sequence):
#     dp_matrix = get_dp_matrix(first_sequence, second_sequence)
#     n_row, n_col = len(first_sequence), len(second_sequence)
#     alignment_cost = get_alignment_cost(n_row, n_col, dp_matrix)
#     return (n_row + n_col - alignment_cost) // 2


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
    # dp_matrix = get_dp_matrix(a, b)
    # print((len(a) + len(b) - dp_matrix[-1][-1]) // 2)
    # for i in dp_matrix:
    #     print(*i, sep='\t')
    # alignment_cost = get_alignment_cost(len(a), len(b), dp_matrix)
    # print(alignment_cost)

