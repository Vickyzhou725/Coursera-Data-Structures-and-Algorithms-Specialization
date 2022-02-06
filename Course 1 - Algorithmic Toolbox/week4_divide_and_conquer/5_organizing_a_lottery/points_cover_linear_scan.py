from sys import stdin
from collections import namedtuple

Event = namedtuple('Event', ['coordinate', 'type', 'index'])


def points_cover_linear(starts, ends, points):
    count = [None] * len(points)

    # to first process all segments that start at this point,
    # then report the number of segments covering it,
    # and then process all segments that end at this point.
    # The needed order is then guaranteed by the lexicographical ordering of these indicators  since l < p < r.
    events = []
    for i in range(len(starts)):
        events.append(Event(starts[i], 'l', i))
        events.append(Event(ends[i], 'r', i))
    for i in range(len(points)):
        events.append(Event(points[i], 'p', i))

    events = sorted(events)
    number_of_segments = 0
    for e in events:
        if e.type == 'l':
            number_of_segments += 1
        elif e.type == 'r':
            number_of_segments -= 1
        elif e.type == 'p':
            count[e.index] = number_of_segments
        else:
            assert False
    return count


from bisect import bisect_left, bisect_right


def points_cover_bisect(starts, ends, points):
    starts, ends = sorted(starts), sorted(ends)
    count = list()
    for index, point in enumerate(points):
        count.append(bisect_right(starts, point) - bisect_left(ends, point))
    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_linear(input_starts, input_ends, input_points)
    print(*output_count)