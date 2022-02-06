# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    points = list()
    segments = sorted(segments, key=lambda s: s.end)
    r = -1
    for segment in segments:
        # if last visit didn't cover this tenant
        # next visit is at this tenant's leaving time
        if r < segment.start:
            r = segment.end
            points.append(r)

    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())   # stop with Ctrl+D
    # print(n)
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # print(input_segments)
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
