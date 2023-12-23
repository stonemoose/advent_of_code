from aocd.models import Puzzle
import numpy as np


def parse(input_data):
    return [line.split() for line in input_data.strip().split("\n")]


def shoelace(corners):
    area = 0
    prev_x, prev_y = corners[0]
    for x, y in corners[1:] + corners[:1]:
        area += prev_x * y
        area -= prev_y * x
        prev_x = x
        prev_y = y
    area = int(abs(area) / 2)
    return area


def solve_part2(parsed):
    corners = [(0, 0)]
    edge = 0
    digit_to_direction = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U",
    }
    for _, _, color in parsed:
        direction = digit_to_direction[color[-2]]
        meters = int(color[2:-2], 16)
        edge += meters
        x, y = corners[-1]
        match direction:
            case "R":
                corners.append((x, y + meters))
            case "L":
                corners.append((x, y - meters))
            case "D":
                corners.append((x + meters, y))
            case "U":
                corners.append((x - meters, y))
    return shoelace(corners) + edge // 2 + 1


def solve(parsed):
    corners = [(0, 0)]
    edge = 0
    for direction, meters, _ in parsed:
        meters = int(meters)
        edge += meters
        x, y = corners[-1]
        match direction:
            case "R":
                corners.append((x, y + meters))
            case "L":
                corners.append((x, y - meters))
            case "D":
                corners.append((x + meters, y))
            case "U":
                corners.append((x - meters, y))
    return shoelace(corners) + edge // 2 + 1


if __name__ == "__main__":
    puzzle = Puzzle(2023, 18)
    example = parse(puzzle.example_data)
    assert solve(example) == 62
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solve(parsed)
    assert solve_part2(example) == 952408144115
    puzzle.answer_b = solve_part2(parsed)
