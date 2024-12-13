import re
from aocd.models import Puzzle
import math


def parse(input_data):
    out = []
    for line in input_data.split("\n\n"):
        nums = [int(n) for n in re.findall(r"[-+]?\d+", line)]
        out.append(
            {
                "A": {
                    "X": nums[0],
                    "Y": nums[1],
                },
                "B": {
                    "X": nums[2],
                    "Y": nums[3],
                },
                "Prize": {
                    "X": nums[4],
                    "Y": nums[5],
                },
            }
        )
    return out


def is_int(num):
    return math.isclose(num, int(num), rel_tol=0, abs_tol=1e-3)


def helper(machine, unit_conversion=False):
    a = machine["A"]
    b = machine["B"]
    price_x = machine["Prize"]["X"]
    price_y = machine["Prize"]["Y"]

    if unit_conversion:
        price_x += 10_000_000_000_000
        price_y += 10_000_000_000_000

    push_b = (price_y * a["X"] - price_x * a["Y"]) / (a["X"] * b["Y"] - b["X"] * a["Y"])
    push_a = (price_x - b["X"] * push_b) / a["X"]

    if is_int(push_a) and is_int(push_b):
        return round(push_a) * 3 + round(push_b)
    return 0


def solve(input_data):
    machines = parse(input_data)
    p1 = p2 = 0

    for machine in machines:
        p1 += helper(machine)
        p2 += helper(machine, True)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 13)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
