from aoc_functionality.util import print_progress_bar

from aocd.models import Puzzle
import numpy as np
import re
from functools import cache
from collections import defaultdict

from itertools import islice


def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))


def get_neighbours(x, y):
    yield (x - 1, y)
    yield (x, y - 1)
    yield (x + 1, y)
    yield (x, y + 1)


def parse(input_data):
    return np.array([list(line) for line in input_data.strip().split("\n")])


def print_garden(virt_garden, gardens, garden):
    for x in range(len(garden)):
        for y in range(len(garden[0])):
            print("O" if (x, y) in gardens[virt_garden] else garden[x, y], end="")
        print()
    print()


def solve(garden, steps_left):
    @cache
    def filled_out(possible_spots):
        for x in range(0, len(garden)):
            for y in range(0, len(garden), 2):
                if not ((x, y) in possible_spots or garden[x, y] == "#"):
                    return False
        return True

    @cache
    def find_possible_spots(possible_spots):
        next_possible_spots = set()
        above = set()
        below = set()
        left = set()
        right = set()
        for old_spot in possible_spots:
            for spot in get_neighbours(*old_spot):
                if spot[0] < 0:
                    above.add((len(garden) - 1, spot[1]))
                elif spot[0] >= len(garden):
                    below.add((0, spot[1]))
                elif spot[1] < 0:
                    left.add((spot[0], len(garden) - 1))
                elif spot[1] >= len(garden):
                    right.add((spot[0], 0))
                elif garden[spot] != "#":
                    next_possible_spots.add(spot)

        return next_possible_spots, above, below, left, right

    x, y = np.where(garden == "S")
    gardens = {(0, 0): frozenset([(x[0], y[0])])}
    ended_gardens = {}

    for steps_taken in range(steps_left):
        if not gardens:
            break
        print_progress_bar(
            steps_taken,
            steps_left - 1,
            suffix=f"{len(set(tuple(g) for g in gardens.values()))}",
        )
        next_gardens = defaultdict(set)
        for virt_garden, spots in gardens.items():
            possible_spots, above, below, left, right = find_possible_spots(
                frozenset(spots)
            )
            if filled_out(frozenset(possible_spots)):
                print(f"filled_out {virt_garden}, len = {len(possible_spots)}")
                print_garden(virt_garden, gardens, garden)
                next_gardens.pop(virt_garden, None)
                if (steps_left - steps_taken) % 2:
                    possible_spots = find_possible_spots(frozenset(possible_spots))[0]
                ended_gardens[virt_garden] = len(possible_spots)
            else:
                next_gardens[virt_garden].update(possible_spots)

            if above:
                if (virt_garden[0] - 1, virt_garden[1]) not in ended_gardens:
                    next_gardens[(virt_garden[0] - 1, virt_garden[1])].update(above)
            if below:
                if (virt_garden[0] + 1, virt_garden[1]) not in ended_gardens:
                    next_gardens[(virt_garden[0] + 1, virt_garden[1])].update(below)
            if left:
                if (virt_garden[0], virt_garden[1] - 1) not in ended_gardens:
                    next_gardens[(virt_garden[0], virt_garden[1] - 1)].update(left)
            if right:
                if (virt_garden[0], virt_garden[1] + 1) not in ended_gardens:
                    next_gardens[(virt_garden[0], virt_garden[1] + 1)].update(right)

        gardens = next_gardens
    ret = sum(len(possible_spots) for possible_spots in gardens.values())
    ret += sum(ended_gardens.values())
    print(f"sum after {steps_taken+1}:", ret)
    return ret


if __name__ == "__main__":
    puzzle = Puzzle(2023, 21)
    example = parse(puzzle.example_data)
    assert solve(example, 6) == 16
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solve(parsed, 64)
    # assert solve(example, 500) == 167004
    # assert solve(example, 26501365) == 16733044
    assert solve(example, 5000) == 16733044
