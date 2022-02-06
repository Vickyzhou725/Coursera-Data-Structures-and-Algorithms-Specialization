# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    n = len(stops)
    new_stops = [0] + stops + [d]
    refills, current_refill = 0, 0
    while current_refill <= n:
        last_refill = current_refill
        # while not arriving destination and next refill stop is achievable
        while (current_refill <= n) and (new_stops[current_refill + 1] - new_stops[last_refill] <= m):
            current_refill += 1
        # mission impossible if can't move to the next refill stop
        if current_refill == last_refill:
            print("Mission impossible")
            return -1
        # refill if not at the destination new_stops[n+1]
        if current_refill <= n:
            refills += 1
    return refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
