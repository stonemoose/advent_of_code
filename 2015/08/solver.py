from aocd.models import Puzzle

puzzle = Puzzle(2015, 8)


def parse(input_data):
    return input_data.strip().split("\n")


def solve(input_data):
    parsed = parse(input_data)
    full = len("".join(parsed))
    represented = len("".join([eval(l) for l in parsed]))
    escaped = len("".join([repr(l).replace('"', '\\"') for l in parsed]))
    return full - represented, escaped - full


puzzle.answer_a, puzzle.answer_b = solve(puzzle.input_data)
