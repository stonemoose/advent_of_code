from aocd.models import Puzzle
from functools import cache
from aoc_functionality.util import profile


def parse(input_data):
    towels, designs = input_data.split("\n\n")
    return frozenset(t for t in towels.split(", ")), designs.split("\n")


@cache
def possible_arrangements(design, towels, longest_towel):
    if not design:
        return 1
    ans = 0
    for i in range(1, min(longest_towel, len(design) + 1)):
        if design[:i] in towels:
            ans += possible_arrangements(design[i:], towels, longest_towel)
    return ans


def solve(input_data):
    towels, designs = parse(input_data)
    longest_towel = max(len(t) for t in towels) + 1
    p1 = p2 = 0
    for design in designs:
        number = possible_arrangements(design, towels, longest_towel)
        p1 += 1 if number else 0
        p2 += number
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 19)
    p1, p2 = profile(solve, puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
