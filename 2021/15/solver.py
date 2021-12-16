import heapq as hq
import numpy as np


def get_neighbours(x, y):
    if x:
        yield (x-1, y)
    if y:
        yield (x, y-1)
    yield (x+1, y)
    yield (x, y+1)


def dijkstra(square, start):
    n = len(square)
    visited = np.full((n, n), False)
    weights = np.full((n, n), np.inf)
    queue = []
    weights[start] = 0
    hq.heappush(queue, (0, start))

    while queue:
        risk, pos = hq.heappop(queue)
        visited[pos] = True
        for pos2 in get_neighbours(*pos):
            try:
                if not visited[pos2]:
                    risk2 = risk + square[pos2]
                    if risk2 < weights[pos2]:
                        weights[pos2] = risk2
                        hq.heappush(queue, (risk2, pos2))
            except IndexError:
                continue
    return weights


def wrap_num(n):
    return np.mod(n, 9) + 1


if __name__ == '__main__':
    with open('input') as f:
        square = np.array([[int(n) for n in line.strip()] for line in f.readlines()])

    print(f'Part 1: {dijkstra(square, (0, 0))[-1][-1]}')

    for axis in (0, 1):
        new_square = np.array(square)
        for _ in range(1, 5):
            new_square = wrap_num(new_square)
            square = np.concatenate((square, new_square), axis=axis)


    print(f'Part 2: {dijkstra(square, (0, 0))[-1][-1]}')
