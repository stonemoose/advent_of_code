import re
from aocd.models import Puzzle


def parse(input_data):
    parsed = []
    for line in input_data.split("\n"):
        parsed.append([int(n) for n in re.findall(r"\d+", line)])
    return parsed


def check_equation(ans, nums, append=False):
    if len(nums) == 1:
        return ans == nums[0]
    if ans < nums[-1]:
        return False

    str_ans = str(ans)
    str_last_num = str(nums[-1])
    return (
        (
            append
            and str_ans.endswith(str_last_num)
            and len(str_ans) > len(str_last_num)
            and check_equation(int(str_ans[: -len(str_last_num)]), nums[:-1], append)
        )
        or (ans % nums[-1] == 0 and check_equation(ans // nums[-1], nums[:-1], append))
        or check_equation(ans - nums[-1], nums[:-1], append)
    )


def solve(input_data):
    parsed = parse(input_data)
    p1 = p2 = 0

    for line in parsed:
        if check_equation(line[0], line[1:]):
            p1 += line[0]
            p2 += line[0]
        elif check_equation(line[0], line[1:], True):
            p2 += line[0]

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 7)

    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
