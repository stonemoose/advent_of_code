from aocd.models import Puzzle


def get_new_position(head, tail):
    if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
        if tail[0] != head[0]:
            tail[0] += 1 if tail[0] < head[0] else -1
        if tail[1] != head[1]:
            tail[1] += 1 if tail[1] < head[1] else -1
    return tail


def solve(input, num_knots):
    knots = [[0, 0] for i in range(num_knots)]
    visited = {(0, 0)}

    for line in input:
        direction, num = line.split()

        for _ in range(int(num)):
            if direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1
            elif direction == "U":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][1] -= 1

            for i in range(1, num_knots):
                knots[i] = get_new_position(knots[i - 1], knots[i])
            visited.add(tuple(knots[-1]))

    return len(visited)


puzzle = Puzzle(2022, 9)
input = puzzle.input_data.strip().split("\n")

puzzle.answer_a = solve(input, 2)
puzzle.answer_b = solve(input, 10)
