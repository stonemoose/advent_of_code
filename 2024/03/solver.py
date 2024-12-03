import re
from aocd.models import Puzzle


def solve(input_data, part2=False):
    regex = r"mul\((\d+),(\d+)\)"
    if part2:
        regex = r"(?s:don't\(\).*?do\(\).*)?" + regex

    return sum((int(n1) * int(n2) for n1, n2 in re.findall(regex, input_data)))


if __name__ == "__main__":
    puzzle = Puzzle(2024, 3)

    ex = puzzle.examples[0]
    if solve(ex.input_data) == ex.answer_a:
        puzzle.answer_a = solve(puzzle.input_data)

    ex2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    if solve(ex2, True) == 48:
        parsed = solve(puzzle.input_data, True)
