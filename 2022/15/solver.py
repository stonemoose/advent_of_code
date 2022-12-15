import re
import numpy as np
from aoc_functionality.loading_bar import print_progress_bar

from aocd.models import Puzzle

puzzle = Puzzle(2022, 15)
input = puzzle.input_data.strip().split("\n")
# input = puzzle.example_data.strip().split("\n")


def update_impossible(x, y, dist, impossible):
    row = 2000000
    # if dist - abs(y - row) < 0:
    #     return

    for x2 in range(x - dist + abs(y - row), x + dist - abs(y - row) + 1):
        impossible[x2] = 1


max_x = 4823751
max_y = 3997568
min_x = -1010425
min_y = -85030

start_distance = []

beacons = set()
for line in input:
    x, y, bx, by = map(int, re.findall("-?\d+", line))
    dist = abs(x - bx) + abs(y - by)
    beacons.add((bx, by))
    start_distance.append([(x, y), dist])

impossible_row = [0] * 6000000
for sensor, dist in start_distance:
    update_impossible(sensor[0], sensor[1], dist, impossible_row)

puzzle.answer_a = sum(impossible_row) - sum(beacon[1] == 2000000 for beacon in beacons)

possible = []
checked_distance = []
i = 0
for sensor, dist in start_distance:
    print_progress_bar(i, len(start_distance) - 1)
    i += 1
    for i in range(2, dist + 2):
        other_dist = dist - i
        maybe_possible = [
            (sensor[0] + i, sensor[1] + other_dist),
            (sensor[0] - i, sensor[1] - other_dist),
            (sensor[0] + other_dist, sensor[1] - i),
            (sensor[0] - other_dist, sensor[1] + i),
        ]
        for x, y in maybe_possible:
            for sensor, dist in start_distance:
                if abs(x - sensor[0]) + abs(y - sensor[1]) <= dist:
                    break
            else:
                print(x, y)
