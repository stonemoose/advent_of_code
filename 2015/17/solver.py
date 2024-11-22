from re import findall
from aocd.models import Puzzle
import functools


def parse(input_data):
    containers = (int(n) for n in input_data.strip().split("\n"))
    return tuple(sorted(containers, reverse=True))


@functools.cache
def solve(containers, liters=150, used=()):
    if liters == 0:
        return 1
    if containers == []:
        return 0
    combinations = 0
    for i, container in enumerate(containers):
        if container <= liters:
            combinations += solve(
                containers[i + 1 :], liters - container, (*used, container)
            )
    return combinations


if __name__ == "__main__":
    puzzle = Puzzle(2015, 17)

    example = (20, 15, 10, 5, 5)
    parsed = parse(puzzle.input_data)
    print(parsed)
    if solve(example, 25) == 4:
        puzzle.answer_a = solve(parsed)
    # puzzle.answer_b =
