from aocd.models import Puzzle
from collections import defaultdict
import numpy as np


def parse(input_data):
    antennas = defaultdict(list)
    lines = input_data.split("\n")
    size_x = len(lines)
    size_y = len(lines[0])
    for x, line in enumerate(lines):
        for y, frequency in enumerate(line):
            if frequency != ".":
                antennas[frequency].append(np.array((x, y), int))
    return antennas, size_x, size_y


def solve(input_data):
    antennas, size_x, size_y = parse(input_data)

    antinodes = set()
    resonant_antinodes = set()
    min_coords = np.array((0, 0), int)
    max_coords = np.array((size_x, size_y), int)

    for frequency in antennas:
        coords = antennas[frequency]
        while coords:
            first = coords.pop(0)
            for second in coords:
                direction_vector = second - first
                direction_vector //= np.gcd(*direction_vector)

                # Part 1
                before = first - direction_vector
                after = second + direction_vector
                if all((min_coords <= before) & (before < max_coords)):
                    antinodes.add(tuple(first - direction_vector))
                if all((min_coords <= after) & (after < max_coords)):
                    antinodes.add(tuple(second + direction_vector))

                # Part 2
                node = first.copy()
                while all((min_coords <= node) & (node < max_coords)):
                    resonant_antinodes.add(tuple(node))
                    node -= direction_vector
                node = first.copy()
                while all((min_coords <= node) & (node < max_coords)):
                    resonant_antinodes.add(tuple(node))
                    node += direction_vector

    return len(antinodes), len(resonant_antinodes)


if __name__ == "__main__":
    puzzle = Puzzle(2024, 8)
    assert solve(puzzle.examples[0].input_data) == (14, 34)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
