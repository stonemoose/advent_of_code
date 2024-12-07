import re
from aocd.models import Puzzle


def parse(input_data):
    parsed = []
    for line in input_data.split("\n"):
        parsed.append([int(n) for n in re.findall(r"\d+", line)])
    return parsed


def check_equation(ans, nums, combined, append=False):
    if not nums:
        return ans == combined
    if combined > ans:
        return False

    return (
        check_equation(ans, nums[1:], combined + nums[0], append)
        or check_equation(ans, nums[1:], combined * nums[0], append)
        or append
        and check_equation(ans, nums[1:], int(str(combined) + str(nums[0])), append)
    )


def solve(input_data):
    parsed = parse(input_data)
    p1 = p2 = 0

    for line in parsed:
        if check_equation(line[0], line[2:], line[1]):
            p1 += line[0]
        if check_equation(line[0], line[2:], line[1], True):
            p2 += line[0]

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 7)

    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
