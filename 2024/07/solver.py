import operator
import re
from aocd.models import Puzzle


def parse(input_data):
    parsed = []
    for line in input_data.split("\n"):
        parsed.append([int(n) for n in re.findall(r"\d+", line)])
    return parsed


def check_equation(ans, nums, operators, combined=None):
    if combined is None:
        combined = nums[0]
        return check_equation(ans, nums[1:], operators, combined)

    if not nums:
        return ans == combined
    if combined > ans:
        return False

    return any(
        check_equation(ans, nums[1:], operators, op(combined, nums[0]))
        for op in operators
    )


def solve(input_data):
    parsed = parse(input_data)
    p1 = p2 = 0
    add_mul = [operator.add, operator.mul]
    append_nums = [lambda x, y: int(str(x) + str(y))]
    all_ops = add_mul + append_nums

    for line in parsed:
        if check_equation(line[0], line[1:], add_mul):
            p1 += line[0]
        if check_equation(line[0], line[1:], all_ops):
            p2 += line[0]

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 7)

    example = puzzle.examples[0]
    ex1, ex2 = solve(example.input_data)
    ex1_ans = 3749
    ex2_ans = 11387
    if ex1_ans:
        assert ex1 == ex1_ans
    if ex2_ans:
        assert ex2 == ex2_ans

    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
