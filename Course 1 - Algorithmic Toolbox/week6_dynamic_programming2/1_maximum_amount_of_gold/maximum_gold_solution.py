from sys import stdin


def knapsack(weights, capacity):
    n = len(weights)
    pack = [[False] * (n+1) for _ in range(capacity+1)]
    pack[0][0] = True

    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] > w:
                # weights[i-1] is not used
                pack[w][i] = pack[w][i-1]
            else:
                pack[w][i] = pack[w][i-1] or pack[w - weights[i-1]][i-1]
    return pack[capacity][n]


def memoized(weights, pack, w, i):
    if (w, i) not in pack:
        if i==0 and w==0:
            pack[(w, i)] = True
        elif i==0 and w>0:
            pack[(w, i)] = False
        elif i>0 and weights[i-1] > w:
            pack[(w, i)] = memoized(weights, pack, w, i-1)
        else:
            pack[(w, i)] = memoized(weights, pack, w, i-1) or \
                           memoized(weights, pack, w-weights[i-1], i - 1)
    return pack[(w, i)]

number_dict = {
'2': ['A', 'B', 'C'],
'3': ['D', 'E', 'F'],
'4': ['G', 'H', 'I'],
'5': ['J', 'K', 'L'],
'6': ['M', 'N', 'O'],
'7': ['P', 'Q', 'R', 'S'],
'8': ['T', 'U', 'V'],
'9': ['W', 'X', 'Y', 'Z'],
'0': ['+'],
}


def phone_number(input, number_dict, output=dict()):
    if input in output.keys():
        return output[input]
    if len(input) == 1:
        output[input] = number_dict[input]
        return output[input]
    if len(input) > 1:
        prev_result = phone_number(input[:-1], number_dict, output=output)
        new_result = number_dict[input[-1]]
        output[input] = [x + y for x in prev_result for y in new_result]
    return output[input]

# backtracking: https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/780232/Backtracking-Python-problems%2B-solutions-interview-prep
# backtracking: https://leetcode.com/problems/generate-parentheses/solution/
# BFS, DFS, tree-traverse, dataframe manipulation, web scrawling, API design, run time analysis
