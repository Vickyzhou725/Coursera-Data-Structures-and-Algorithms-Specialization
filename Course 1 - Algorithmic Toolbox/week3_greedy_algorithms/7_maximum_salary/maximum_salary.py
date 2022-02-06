# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_greater_or_equal(digit, max_digit):
    return str(digit)+str(max_digit) >= str(max_digit) + str(digit)


def sort_number_string_descending(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if is_greater_or_equal(numbers[j], numbers[i]):
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers


def largest_number(numbers):
    answer = ''
    sorted_numbers = sort_number_string_descending(numbers)
    for number in sorted_numbers:
        answer += str(number)
    return answer


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
