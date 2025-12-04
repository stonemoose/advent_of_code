from aocd.models import Puzzle


def parse(input_data):
    parsed = []
    width = len(input_data.split()[0]) + 2
    parsed.append([0] * width)
    for line in input_data.split():
        parsed.append([0] + [int(c == "@") for c in line] + [0])
    parsed.append([0] * width)
    return parsed


def find_accessible(rolls):
    accessible = set()
    for x in range(len(rolls)):
        for y in range(len(rolls[0])):
            if rolls[x][y]:
                neighbours = -1
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        neighbours += rolls[x + i][y + j]
                if neighbours < 4:
                    accessible.add((x, y))
    return accessible


def solve(input_data):
    p1 = p2 = 0
    rolls = parse(input_data)

    removable = find_accessible(rolls)
    p1 = len(removable)
    while removable:
        p2 += len(removable)
        for x, y in removable:
            rolls[x][y] = 0
        removable = find_accessible(rolls)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 4)
    p1, p2 = solve(puzzle.input_data)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
