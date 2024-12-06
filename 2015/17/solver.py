from re import findall
from aocd.models import Puzzle
import functools


def parse(input_data):
    containers = (int(n) for n in input_data.strip().split("\n"))
    return tuple(sorted(containers, reverse=True))


@functools.cache
def solver(containers, liters=150, used=()):
    if liters == 0:
        return 1
    if containers == []:
        return 0
    combinations = 0
    for i, container in enumerate(containers):
        if container <= liters:
            combinations += solver(
                containers[i + 1 :], liters - container, (*used, container)
            )
    return combinations


def solve(input_data, liters=150):
    parsed = parse(input_data)
    p1 = solver(parsed, liters=liters)
    p2 = 0
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2015, 17)

    ex1, ex2 = solve(puzzle.examples[0].input_data, liters=25)
    p1, p2 = solve(puzzle.input_data)
    assert ex1 == int(puzzle.examples[0].answer_a)
    puzzle.answer_a = p1
    assert ex2 == int(puzzle.examples[0].answer_b)
    puzzle.answer_b = p2
