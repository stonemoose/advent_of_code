from aocd.models import Puzzle


def parse(input_data):
    return [[int(n) for n in line.split()] for line in input_data.strip().split("\n")]


def extrapolate(sequence):
    differences = []
    current = sequence[0]
    for n in sequence[1:]:
        differences.append(n - current)
        current = n
    if len(set(differences)) == 1:
        past = differences[0]
        future = differences[-1]
    else:
        past, future = extrapolate(differences)
    return sequence[0] - past, sequence[-1] + future


def solve(input_data):
    parsed_data = parse(input_data)
    p1 = p2 = 0
    for line in parsed_data:
        past, future = extrapolate(line)
        p1 += future
        p2 += past

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2023, 9)

    if solve(puzzle.example_data) == (114, 2):
        puzzle.answer_a, puzzle.answer_b = solve(puzzle.input_data)
