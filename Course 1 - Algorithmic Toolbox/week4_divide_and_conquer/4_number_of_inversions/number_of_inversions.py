# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def merge_sort(array):
    length = len(array)
    if length == 1:
        return array, 0
    mid = length // 2
    left_array, left_inverse = merge_sort(array[:mid])
    right_array, right_inverse = merge_sort(array[mid:])
    sorted_array, array_inverse = merge(left_array, right_array)
    return sorted_array, left_inverse + right_inverse + array_inverse


def merge(left_array, right_array):
    # number of pairs (l, r) in (left_array, right_array) respectively and l > r
    sorted_array = list()
    array_inverse = 0
    while (len(left_array) > 0) and (len(right_array) > 0):
        l = left_array[0]
        r = right_array[0]
        if l <= r:
            sorted_array.append(l)
            left_array.pop(0)
        elif l > r:
            sorted_array.append(r)
            right_array.pop(0)
            array_inverse += 1
    # at least one list is empty
    sorted_array.extend(left_array)
    sorted_array.extend(right_array)

    return sorted_array, array_inverse


def compute_inversions(a):
    sorted_array, inversion_numbers = merge_sort(a)
    # print(sorted_array)
    return inversion_numbers


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
