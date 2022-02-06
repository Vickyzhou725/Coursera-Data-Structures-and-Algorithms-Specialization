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
    return dp_matrix


def get_max_common_sequences(i, j, dp_matrix, first_sequence, second_sequence):
    # total_elements = 2 * match + 2 * mismatch + 1 * insertion + 1 * deletion
    # edit_distance = 0 * match + 2 * mismatch + 1 * insertion + 1 * deletion
    # alignment_cost = 0 * match + 2 * mismatch + 1 * insertion + 1 * deletion
    max_common_sequences = [[]]
    if (i != 0) and (j != 0):
        max_common_sequences = []
        if (i >= 1) and (j >= 1) and (dp_matrix[i][j] == dp_matrix[i-1][j-1] + 2):    # 2 * mismatch
            mismatch_common_sequences = get_max_common_sequences(i-1, j-1, dp_matrix, first_sequence, second_sequence)
            for seq in mismatch_common_sequences:
                if seq not in max_common_sequences:
                    max_common_sequences.append(seq)
        if (i >= 1) and (dp_matrix[i][j] == dp_matrix[i-1][j] + 1):  # 1 * insertion
            insertion_common_sequences = get_max_common_sequences(i-1, j, dp_matrix, first_sequence, second_sequence)
            for seq in insertion_common_sequences:
                if seq not in max_common_sequences:
                    max_common_sequences.append(seq)
        if (j >= 1) and (dp_matrix[i][j] == dp_matrix[i][j-1] + 1):  # 1 * deletion
            deletion_common_sequences = get_max_common_sequences(i, j-1, dp_matrix, first_sequence, second_sequence)
            for seq in deletion_common_sequences:
                if seq not in max_common_sequences:
                    max_common_sequences.append(seq)
        if (i >= 1) and (j >= 1) and (dp_matrix[i][j] == dp_matrix[i-1][j-1]) and (first_sequence[i-1] == second_sequence[j-1]):    # 0 * match
            match_common_sequences = get_max_common_sequences(i-1, j-1, dp_matrix, first_sequence, second_sequence)
            match_common_sequences = [x + [first_sequence[i-1]] for x in match_common_sequences]
            for seq in match_common_sequences:
                if seq not in max_common_sequences:
                    max_common_sequences.append(seq)
    return max_common_sequences


def get_max_common_sequences_from_lists(max_common_sequences1, max_common_sequences2, max_sequence_length, max_common_sequences):
    for seq1 in max_common_sequences1:
        for seq2 in max_common_sequences2:
            dp_matrix = lcs2(seq1, seq2)
            max_seq_len = (len(seq1) + len(seq2) - dp_matrix[-1][-1]) // 2
            if max_sequence_length <= max_seq_len:
                max_sequence_length = max_seq_len
                max_common_seq = get_max_common_sequences(len(seq1), len(seq2), dp_matrix, seq1, seq2)
                if max_sequence_length < max_seq_len:
                    max_common_sequences = max_common_seq
                else:
                    for seq in max_common_seq:
                        if seq not in max_common_sequences:
                            max_common_sequences.append(seq)
    return max_sequence_length, max_common_sequences


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    dp_matrix1 = lcs2(first_sequence, second_sequence)
    max_common_sequences1 = get_max_common_sequences(len(first_sequence), len(second_sequence), dp_matrix1, first_sequence, second_sequence)
    dp_matrix2 = lcs2(first_sequence, third_sequence)
    max_common_sequences2 = get_max_common_sequences(len(first_sequence), len(third_sequence), dp_matrix2, first_sequence, third_sequence)
    dp_matrix3 = lcs2(second_sequence, third_sequence)
    max_common_sequences3 = get_max_common_sequences(len(second_sequence), len(third_sequence), dp_matrix3, second_sequence, third_sequence)

    max_sequence_length, max_common_sequences = 0, list()
    max_sequence_length, max_common_sequences = get_max_common_sequences_from_lists(max_common_sequences1, max_common_sequences2, max_sequence_length, max_common_sequences)
    max_sequence_length, max_common_sequences = get_max_common_sequences_from_lists(max_common_sequences1, max_common_sequences3, max_sequence_length, max_common_sequences)
    max_sequence_length, max_common_sequences = get_max_common_sequences_from_lists(max_common_sequences2, max_common_sequences3, max_sequence_length, max_common_sequences)

    # print(max_common_sequences)
    return max_sequence_length


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
