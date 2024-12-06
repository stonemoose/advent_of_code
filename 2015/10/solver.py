from aocd.models import Puzzle


def parse(input_data):
    return list(input_data)


def solver(sequence, iterations):
    for i in range(iterations):
        next = []
        current = sequence[0]
        amount = 0
        for i in sequence:
            if i == current:
                amount += 1
            else:
                next += [str(amount), current]
                amount = 1
                current = i
        sequence = next + [str(amount), i]

    sequence = "".join(sequence)
    return len(sequence)


def solve(input_data):
    parsed = parse(input_data)
    p1 = solver(parsed, 40)
    p2 = solver(parsed, 50)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2015, 10)
    puzzle.answer_a = solver(parse(puzzle.input_data), 40)
    puzzle.answer_b = solver(parse(puzzle.input_data), 50)
