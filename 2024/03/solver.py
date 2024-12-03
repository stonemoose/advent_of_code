import re
from aocd.models import Puzzle


def solve(input_data, part2=False):
    regex = r"mul\((\d+),(\d+)\)"
    if part2:
        end_disabled = re.search(r"(?s:don't\(\)(?:(?!do\(\)).)*$)", input_data)
        if end_disabled:
            input_data = input_data[:end_disabled.start()]
        regex = r"(?s:don't\(\).*?do\(\).*?)?" + regex
    return sum((int(n1) * int(n2) for n1, n2 in re.findall(regex, input_data)))


if __name__=="__main__":
    puzzle = Puzzle(2024, 3)

    ex = puzzle.examples[0]
    assert solve(ex.input_data) == 161
    puzzle.answer_a = solve(puzzle.input_data)

    ex2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    assert solve(ex2, part2=True) == 48
    puzzle.answer_b = solve(puzzle.input_data, part2=True)

