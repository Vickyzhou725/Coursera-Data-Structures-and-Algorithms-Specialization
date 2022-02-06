# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')
# Point = namedtuple('Point2D',['x','y'])
# Point = namedtuple('Point2D',('x','y'))
# Point = namedtuple('Point2D',('x, y'))
# Point = namedtuple('Point2D','x y')
# Named tuples allow you to create tuples and assign meaningful names to the positions of the tuple’s elements.


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points):
    if len(points) <= 1:
        return float('inf')
    if len(points) == 2:
        return sqrt(
            (points[0].x - points[1].x) ** 2 +
            (points[0].y - points[1].y) ** 2
        )
    points = sorted(points, key=lambda point: point.x)
    mid = len(points) // 2
    left_min_d = minimum_distance_squared(points[:mid])
    right_min_d = minimum_distance_squared(points[mid:])
    d = min(left_min_d, right_min_d)

    # find min_d < d where p1 in left plane and p2 in right plane
    # only need to consider p1 and p2 that x-axis within d to points[mid] O(n)
    strip_points = [p for p in points if abs(p.x - points[mid].x) < d]
    strip_points = sorted(strip_points, key=lambda point: point.y)
    n = len(strip_points)
    min_d = d
    for i in range(n):
        for j in range(1, 7):
            if i + j < n:
                min_d = min(
                    min_d,
                    minimum_distance_squared([strip_points[i], strip_points[i+j]])
                )
    return min_d


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
