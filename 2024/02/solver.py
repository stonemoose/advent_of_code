import re
from aocd.models import Puzzle


def parse(input_data):
    out = []
    for line in input_data.strip().split("\n"):
        nums = re.findall(r"\d+", line)
        out.append([int(n) for n in nums])
    return out


def is_safe(levels):
    increasing = levels[1] > levels[0]
    last = levels[0]
    for current in levels[1:]:
        if not abs(current - last) in (1, 2, 3):
            return False
        if increasing != (current > last):
            return False
        last = current
    return True


def num_safe_reports(parsed, problem_dampener=False):
    ans = 0
    for line in parsed:
        if is_safe(line):
            ans += 1
        elif problem_dampener:
            for i in range(len(line)):
                copied_line = list(line)
                copied_line.pop(i)
                if is_safe(copied_line):
                    ans += 1
                    break
    return ans


def solve(input_data):
    parsed = parse(input_data)
    p1 = num_safe_reports(parsed)
    p2 = num_safe_reports(parsed, True)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 2)

    parsed = parse(puzzle.input_data)

    for example in puzzle.examples:
        assert num_safe_reports(parse(example.input_data)) == int(example.answer_a)
    puzzle.answer_a = num_safe_reports(parsed)

    for example in puzzle.examples:
        assert num_safe_reports(parse(example.input_data), True) == int(
            example.answer_b
        )
    puzzle.answer_b = num_safe_reports(parsed, True)
