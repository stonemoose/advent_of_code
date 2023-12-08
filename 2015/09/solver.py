import itertools
from collections import defaultdict
import math

from aocd.models import Puzzle

puzzle = Puzzle(2015, 9)


def parse(input_data):
    distances = defaultdict(dict)
    for line in input_data.split("\n"):
        start, _, end, _, distance = line.split()
        distances[start][end] = int(distance)
        distances[end][start] = int(distance)
    return distances


def solve(parsed):
    best = math.inf
    worst = 0

    for path in itertools.permutations(parsed):
        length = 0
        current = path[0]
        for next in path[1:]:
            length += parsed[current][next]
            current = next
        best = min(best, length)
        worst = max(worst, length)

    return best, worst


puzzle.answer_a, puzzle.answer_b = solve(parse(puzzle.input_data))
