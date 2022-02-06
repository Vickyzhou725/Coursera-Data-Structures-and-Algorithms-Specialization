# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def binary_search_lower(array, query, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left > right:
        return left
    mid = (left + right) // 2
    if query <= array[mid]:
        return binary_search_lower(array, query, left=left, right=mid-1)
    elif query > array[mid]:
        return binary_search_lower(array, query, left=mid+1, right=right)


def binary_search_upper(array, query, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left > right:
        return left
    mid = (left + right) // 2
    if query >= array[mid]:
        return binary_search_upper(array, query, left=mid+1, right=right)
    elif query < array[mid]:
        return binary_search_upper(array, query, left=left, right=mid - 1)


def merge(left_array, right_array):
    sorted_array = list()
    while (len(left_array) > 0) and (len(right_array) > 0):
        l = left_array[0]
        r = right_array[0]
        if l <= r:
            sorted_array.append(l)
            left_array.pop(0)
        else:
            sorted_array.append(r)
            right_array.pop(0)
    # at least one array is empty
    sorted_array.extend(left_array)
    sorted_array.extend(right_array)
    return sorted_array


def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    sorted_array = merge(left_array, right_array)
    return sorted_array


def points_cover(starts, ends, points):
    # 1. sort by point ends [O(nlogn)]
    sorted_ends = merge_sort(ends)
    ends_before_p = [0] * len(points)
    # binary search for m points in list of length n [m * O(logn)]
    # lower search for segments ends before p, [3, 3, 4, 5] for 3 return 0
    for i in range(len(points)):
        ends_before_p[i] += binary_search_lower(sorted_ends, points[i])

    # 2. sort by point starts [O(nlogn)]
    sorted_starts = merge_sort(starts)
    starts_before_p = [0] * len(points)
    # binary search for m points in list of length n [m * O(logn)]
    # upper search for segments starts before p, [3, 3, 4, 5] for 3 return 2
    for i in range(len(points)):
        starts_before_p[i] += binary_search_upper(sorted_starts, points[i])

    # 3. cover_p = starts_before_p - ends_before_p
    cover_p = list()
    for i in range(len(points)):
        cover_p.append(starts_before_p[i] - ends_before_p[i])

    return cover_p


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
