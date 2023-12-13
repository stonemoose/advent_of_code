from aocd.models import Puzzle
from aoc_functionality.util import Color
import itertools


def parse(input_data):
    return [[c for c in line] for line in input_data.strip().split("\n")]


def expanded_manhatten_distance(point1, point2, expand, empty_x_and_y):
    distance = 0
    for i in range(2):
        smallest = min(point1[i], point2[i])
        biggest = max(point1[i], point2[i])
        for empty_line in empty_x_and_y[i]:
            if smallest < empty_line < biggest:
                distance += expand - 1
        distance += biggest - smallest
    return distance


def print_map(universe, empty_y, empty_x):
    for y, line in enumerate(universe):
        for x, c in enumerate(line):
            if y in empty_y and x in empty_x:
                print("╋", end="")
            elif y in empty_y:
                print("━", end="")
            elif x in empty_x:
                print("┃", end="")
            elif c == "#":
                print(Color.YELLOW + "★" + Color.END, end="")
            else:
                print(" ", end="")
        print()


def solve(universe, expand=2, should_print=False):
    empty_y = []
    empty_x = []
    for i in range(len(universe[0])):
        v_line = [l[i] for l in universe]
        if len(set(v_line)) == 1:
            empty_x.append(i)

    for i, line in enumerate(universe):
        if len(set(line)) == 1:
            empty_y.append(i)

    if should_print:
        print_map(universe, empty_y, empty_x)

    galaxies = []
    for y, line in enumerate(universe):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((x, y))

    total_dist = 0
    for coord1, coord2 in itertools.combinations(galaxies, 2):
        total_dist += expanded_manhatten_distance(
            coord1, coord2, expand, (empty_x, empty_y)
        )

    print(total_dist)
    return total_dist


if __name__ == "__main__":
    puzzle = Puzzle(2023, 11)

    parsed_ex = parse(puzzle.example_data)
    assert solve(parsed_ex) == 374
    assert solve(parsed_ex, 10) == 1030
    assert solve(parsed_ex, 100, True) == 8410
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solve(parsed)
    puzzle.answer_b = solve(parsed, 1_000_000, True)
