# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements, left=0, right=None):
    assert len(elements) <= 10 ** 5
    # if an element is the majority of the array, it must be the majority of at least one of its subarray
    # check if the majority elements in the sub arrays exceed n/2
    # T(n) = 2 * T(n/2) + O(n) => O(nlogn)
    length = len(elements)
    if right is None:
        right = length - 1
    if left > right:
        return -1
    if left == right:
        return elements[left]
    mid = (left + right) // 2
    majority_left = majority_element(elements, left=left, right=mid)
    majority_right = majority_element(elements, left=mid+1, right=right)

    count_left, count_right = 0, 0
    for i in elements:
        if i == majority_left:
            count_left += 1
        elif i == majority_right:
            count_right += 1
    if count_right > length/2:
        return majority_right
    elif count_left > length/2:
        return majority_left
    else:
        return -1


def majority_hash_map(elements):
    # O(n)
    hash_map = dict()
    for i in elements:
        if i not in hash_map.keys():
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    n = len(elements)
    for key, value in hash_map.items():
        if value > n/2:
            return key
    return -1


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
    print(majority_hash_map(input_elements))
