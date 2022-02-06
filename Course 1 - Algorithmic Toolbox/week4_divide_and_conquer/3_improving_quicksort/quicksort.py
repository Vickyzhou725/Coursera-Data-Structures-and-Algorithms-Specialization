# python3

from random import randint


def partition3(array, left, right):
    x = array[left]
    mid1, mid2 = left, left
    for i in range(left+1, right+1):
        y = array[i]
        if x > y:
            mid1 += 1
            array[i], array[mid1] = array[mid1], array[i]
        if x >= y:
            mid2 += 1
            # allowing for scenario of no duplicate
            if array[i] <= array[mid2]:
                array[i], array[mid2] = array[mid2], array[i]
    array[left], array[mid1] = array[mid1], array[left]
    return mid1, mid2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    # partition so that mid1-mid2 are in their final position
    mid1, mid2 = partition3(array, left, right)
    randomized_quick_sort(array, left, mid1-1)
    randomized_quick_sort(array, mid2+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
