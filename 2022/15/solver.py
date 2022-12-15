import re
import numpy as np
from aoc_functionality.util import print_progress_bar, profile

from aocd.models import Puzzle


def main():
    def get_edges2(x, y, dist):
        window = 4_000_000
        window = 20
        edges = set()
        for x2 in range(max(0, x - dist), min(window, x + dist + 1)):
            for edge in ((x2, y - (x - x2)), (x2, y - (x - x2))):
                if 0 <= edge[0] <= window and 0 <= edge[1] <= window:
                    edges.add(edge)
        return edges

    def get_edges(x, y, dist):
        window = 4_000_000
        window = 20
        edges = set()
        for i in range(dist):
            other_dist = abs(dist + 1 - i)
            for edge in (
                (x + i, y + other_dist),
                (x - i, y - other_dist),
                (x + other_dist, y - i),
                (x - other_dist, y + i),
            ):
                if 0 <= edge[0] <= window and 0 <= edge[1] <= window:
                    edges.add(edge)
        return edges

    puzzle = Puzzle(2022, 15)
    input = puzzle.input_data.strip().split("\n")
    input = puzzle.example_data.strip().split("\n")

    sensor_distance = []
    possible = set()
    all_edges = set()
    for i, line in enumerate(input):
        # print_progress_bar(i, len(input) - 1)
        x, y, bx, by = map(int, re.findall("-?\d+", line))
        dist = abs(x - bx) + abs(y - by)
        sensor_distance.append([(x, y), dist])

        edges = get_edges2(x, y, dist)
        possible.update(edges & all_edges)
        all_edges.update(edges)

    n = 0
    print(f"possible: {len(possible)}")
    print(f"all edges in window: {len(all_edges)}")
    for x, y in possible:
        # print_progress_bar(n, len(possible) - 1)
        n += 1
        for sensor, dist in sensor_distance:
            if abs(x - sensor[0]) + abs(y - sensor[1]) <= dist:
                break
        else:
            print()
            print(x, y, x * 4000000 + y)
            return


profile(main)
