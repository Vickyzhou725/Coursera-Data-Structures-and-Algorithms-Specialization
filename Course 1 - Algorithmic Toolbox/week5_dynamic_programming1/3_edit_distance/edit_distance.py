# python3


def edit_distance(first_string, second_string):
    # from first string (row) to second string (col)
    # note can't use [[-1] * n_col] * n_row
    # can't initialize the first column to different values
    n_col, n_row = len(first_string)+1, len(second_string)+1
    dp_matrix = [[x for x in range(n_col)]] + [[x] + [-1] * (n_col-1) for x in range(1, n_row)]
    for i in range(1, n_row):
        for j in range(1, n_col):
            deletion = dp_matrix[i-1][j] + 1
            insertion = dp_matrix[i][j-1] + 1
            if second_string[i-1] == first_string[j-1]:
                replace = dp_matrix[i - 1][j - 1]
            else:
                replace = dp_matrix[i-1][j-1] + 1
            dp_matrix[i][j] = min(deletion, insertion, replace)
    return dp_matrix[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # for i in dp_matrix:
    #     print(*i, sep='\t')