from aocd.models import Puzzle
from collections import defaultdict
from functools import cache


def parse(input_data):
    return input_data.split("\n")


def manhatten_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


@cache
def get_shortest_directional(current, next_button):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    pad = [" ^A", "<v>"]
    for x, line in enumerate(pad):
        for y, char in enumerate(line):
            if char == current:
                curr_x, curr_y = x, y
            if char == next_button:
                next_x, next_y = x, y
    x_diff = curr_x - next_x
    y_diff = curr_y - next_y
    corner_problem = False
    if (curr_y == 0 and next_x == 0) ^ (next_y == 0 and curr_x == 0):
        corner_problem = True

    string = ""

    if x_diff > 0:
        string += "^" * x_diff
    elif x_diff < 0:
        string += "v" * -x_diff

    if y_diff > 0:
        if corner_problem:
            string += "<" * y_diff
        else:
            string = "<" * y_diff + string
    elif y_diff < 0:
        if corner_problem:
            string = ">" * -y_diff + string
        else:
            string += ">" * -y_diff

    return string + "A"


@cache
def get_shortest_numeric(current, next_button):
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """
    pad = ["789", "456", "123", " 0A"]
    for x, line in enumerate(pad):
        for y, char in enumerate(line):
            if char == current:
                curr_x, curr_y = x, y
            if char == next_button:
                next_x, next_y = x, y
    x_diff = curr_x - next_x
    y_diff = curr_y - next_y
    corner_problem = False
    if (curr_y == 0 and next_x == 3) ^ (next_y == 0 and curr_x == 3):
        corner_problem = True

    string = ""

    if x_diff > 0:
        string += "^" * x_diff
    elif x_diff < 0:
        string += "v" * -x_diff

    if y_diff > 0:
        if corner_problem:
            string += "<" * y_diff
        else:
            string = "<" * y_diff + string
    elif y_diff < 0:
        if corner_problem:
            string = ">" * -y_diff + string
        else:
            string += ">" * -y_diff

    return string + "A"


def get_full_shortest_num(line):
    code = defaultdict(int)
    line = "A" + line
    first_move = get_shortest_numeric(line[0], line[1])
    for first, second in zip(line[1:-1], line[2:]):
        code[get_shortest_numeric(first, second)] += 1
    return first_move, code


def get_full_shortest_dir(first_press, code):
    next_code = defaultdict(int)
    line = "A" + first_press
    first_move = ""
    for first, second in zip(line[:-1], line[1:]):
        first_move += get_shortest_directional(first, second)

    first_moves = first_move.split("A")[:-1]
    before_a = first_moves[0] + "A"
    for other in first_moves[1:]:
        next_code[other + "A"] += 1

    for line, amount in code.items():
        line = "A" + line
        for first, second in zip(line[:-1], line[1:]):
            next_code[get_shortest_directional(first, second)] += amount
    return before_a, next_code


def helper(line, directional=3):
    first_press, code = get_full_shortest_num(line)
    for _ in range(1, directional):
        first_press, code = get_full_shortest_dir(first_press, code)

    code_len = len(first_press)
    for code, amount in code.items():
        code_len += len(code) * amount
    return code_len * int(line[:-1])


def solve(input_data):
    parsed = parse(input_data)
    p1 = p2 = 0
    for line in parsed:
        p1 += helper(line, 3)
        p2 += helper(line, 26)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 21)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
