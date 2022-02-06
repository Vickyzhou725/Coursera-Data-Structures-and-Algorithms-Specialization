# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query, left=0, right=None):
    assert all(keys[i] <= keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    if right is None:
        right = len(keys) - 1
    # iterative version
    while left <= right:
        mid = (left + right) // 2
        if query <= keys[mid]:
            right = mid - 1
        elif query > keys[mid]:
            left = mid + 1
    if (left >= 0) and (left < len(keys)) and (query == keys[left]):
        return left
    else:
        return left


def binary_search_iterative(keys, query, left=0, right=None):
    assert all(keys[i] <= keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    if right is None:
        right = len(keys) - 1
    # iterative version
    while left <= right:
        mid = (left + right) // 2
        if query >= keys[mid]:
            left = mid + 1
        elif query < keys[mid]:
            right = mid - 1
    if (right >= 0) and (right < len(keys)) and (query == keys[right]):
        return right
    else:
        return right + 1


# def binary_search_recursive(keys, query, left=0, right=None):
#     assert all(keys[i] <= keys[i + 1] for i in range(len(keys) - 1))
#     assert 1 <= len(keys) <= 3 * 10 ** 4
#
#     if right is None:
#         right = len(keys) - 1
#     # recursive version
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if query < keys[mid]:
#         return binary_search_recursive(keys, query, left=left, right=mid-1)
#     elif query > keys[mid]:
#         return binary_search_recursive(keys, query, left=mid+1, right=right)
#     else:
#         return mid


def binary_search_lower(keys, query, left=0, right=None):
    assert all(keys[i] <= keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    if right is None:
        right = len(keys) - 1
    # recursive version
    if left > right:
        if (left >= 0) and (left < len(keys)) and (query == keys[left]):
            return left
        else:
            return left
    mid = (left + right) // 2
    if query <= keys[mid]:
        return binary_search_lower(keys, query, left=left, right=mid-1)
    elif query > keys[mid]:
        return binary_search_lower(keys, query, left=mid+1, right=right)


def binary_search_upper(keys, query, left=0, right=None):
    assert all(keys[i] <= keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    if right is None:
        right = len(keys) - 1
    # recursive version
    if left > right:
        if (right >= 0) and (right < len(keys)) and (query == keys[right]):
            return right
        else:
            return right + 1
    mid = (left + right) // 2
    if query >= keys[mid]:
        return binary_search_upper(keys, query, left=mid+1, right=right)
    elif query < keys[mid]:
        return binary_search_upper(keys, query, left=left, right=mid-1)


if __name__ == '__main__':
    keys_length = int(input())
    input_keys = list(map(int, input().split()))
    queries_length = int(input())
    input_queries = list(map(int, input().split()))

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
    print('\n')
    for q in input_queries:
        print(binary_search_iterative(input_keys, q), end=' ')
    print('\n')
    for q in input_queries:
        print(binary_search_lower(input_keys, q), end=' ')
    print('\n')
    for q in input_queries:
        print(binary_search_upper(input_keys, q), end=' ')
