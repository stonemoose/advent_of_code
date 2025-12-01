from aocd.models import Puzzle


def parse(input_data):
    return [(line[0], int(line[1:].strip())) for line in input_data.split()]


def solve(input_data):
    p1 = p2 = 0
    dial = 50
    turns = parse(input_data)
    for direction, amount in turns:
        for _ in range(amount):
            if direction == "R":
                dial += 1
            else:
                dial -= 1
            dial %= 100
            if dial == 0:
                p2 += 1
        if dial == 0:
            p1 += 1
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 1)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
