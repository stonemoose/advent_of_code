from aocd.models import Puzzle

puzzle = Puzzle(2015, 10)


def parse(input_data):
    return list(input_data)


def solve(sequence, iterations):
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


puzzle.answer_a = solve(parse(puzzle.input_data), 40)
puzzle.answer_b = solve(parse(puzzle.input_data), 50)
