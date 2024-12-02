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


def solve(parsed, problem_dampener=False):
    ans = 0
    for line in parsed:
        if problem_dampener:
            for i in range(len(line)):
                copied_line = list(line)
                copied_line.pop(i)
                if is_safe(copied_line):
                    ans += 1
                    break
            else:
                ans += is_safe(line)
        else:
            ans += is_safe(line)
    return ans


if __name__ == "__main__":
    puzzle = Puzzle(2024, 2)

    parsed = parse(puzzle.input_data)

    for example in puzzle.examples:
        assert solve(parse(example.input_data)) == int(example.answer_a)
    puzzle.answer_a = solve(parsed)

    for example in puzzle.examples:
        assert solve(parse(example.input_data), True) == int(example.answer_b)
    puzzle.answer_b = solve(parsed, True)
