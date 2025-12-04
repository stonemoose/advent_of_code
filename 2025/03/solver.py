from aocd.models import Puzzle


def parse(input_data):
    parsed = []
    for line in input_data.split():
        parsed.append([int(c) for c in line] + [0])
    return parsed


def highest_jump(bank, batteries):
    jump = 0
    start = 0
    for end in range(batteries, 0, -1):
        highest = max(bank[start:-end])
        start += bank[start:-end].index(highest) + 1
        jump += highest * 10 ** (end - 1)
    return jump


def solve(input_data):
    p1 = p2 = 0
    banks = parse(input_data)
    for bank in banks:
        p1 += highest_jump(bank, 2)
        p2 += highest_jump(bank, 12)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 3)
    p1, p2 = solve(puzzle.input_data)
    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
