from aocd.models import Puzzle


def solver(inputs):
    accumulator = 0
    visited = []
    counter = 0

    while True:
        op, num = inputs[counter]
        visited.append(counter)
        num = int(num)
        if op == "acc":
            accumulator += num
            counter += 1
        if op == "jmp":
            counter += num
        if op == "nop":
            counter += 1
        if counter in visited:
            break
        if counter >= len(inputs):
            break
    return visited, accumulator


def solve(input_data):
    inputs = [line.split() for line in input_data.split("\n")]
    visited, p1 = solver(inputs)

    # assume the last jump is the problematic one
    inputs[visited[-1]][0] = "nop"
    _, p2 = solver(inputs)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 8)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
