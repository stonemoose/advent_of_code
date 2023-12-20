from aocd.models import Puzzle
import heapq as hq
import numpy as np


def parse(input_data):
    return np.array(
        [[int(char) for char in line] for line in input_data.strip().split("\n")]
    )


def print_map(parsed):
    for line in parsed:
        print("".join(map(str, line)))


def get_horizontal_neighbors(x, y, max_val, reach=3):
    for above_y in range(max(0, y - reach), y):
        yield (x, above_y)
    for bellow_y in range(y + 1, min(max_val, y + reach + 1)):
        yield (x, bellow_y)


def get_horizontal_neighbors(x, y, max_val, reach=3):
    for before_x in range(max(0, x - reach), x):
        yield (before_x, y)
    for after_x in range(x + 1, min(max_val, x + reach + 1)):
        yield (after_x, y)


def get_neighbours(x, y):
    if x:
        yield (x - 1, y)
    if y:
        yield (x, y - 1)
    yield (x + 1, y)
    yield (x, y + 1)


def dijkstra(square, start):
    n = len(square)
    visited = np.full((n, n), False)
    vertical_weights = np.full((n, n), np.inf)
    horizontal_weights = np.full((n, n), np.inf)
    queue = []
    vertical_weights[start] = horizontal_weights[start] = 0
    hq.heappush(queue, (0, "horizontal", start))
    hq.heappush(queue, (0, "vertical", start))

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


def solve(parsed):
    start = (0, 0)
    end = (len(parsed) - 1, len(parsed[0]) - 1)
    print_map(parsed)
    dijkstra_split(start, parsed, end)
    print(end)


if __name__ == "__main__":
    puzzle = Puzzle(2023, 17)

    parsed_ex = parse(puzzle.example_data)
    assert solve(parsed_ex) == 102
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solve(parsed)
