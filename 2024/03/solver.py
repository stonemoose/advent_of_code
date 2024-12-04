import re
from aocd.models import Puzzle


def sum_mul(input_data, part2=False):
    regex = r"mul\((\d+),(\d+)\)"
    if part2:
        end_disabled = re.search(r"(?s:don't\(\)(?:(?!do\(\)).)*$)", input_data)
        if end_disabled:
            input_data = input_data[: end_disabled.start()]
        regex = r"(?s:don't\(\).*?do\(\).*?)?" + regex
    return sum((int(n1) * int(n2) for n1, n2 in re.findall(regex, input_data)))


def solve(input_data):
    return sum_mul(input_data), sum_mul(input_data, True)


if __name__ == "__main__":
    puzzle = Puzzle(2024, 3)

    ex = puzzle.examples[0]
    assert sum_mul(ex.input_data) == 161
    puzzle.answer_a = sum_mul(puzzle.input_data)

    ex2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    assert sum_mul(ex2, part2=True) == 48
    puzzle.answer_b = sum_mul(puzzle.input_data, part2=True)
