from aocd.models import Puzzle


def parse(input_data):
    return [line.split("\n") for line in input_data.strip().split("\n\n")]


def mirror_point(rock):
    for i in range(1, len(rock)):
        if i > len(rock) // 2:
            if rock[i - (len(rock) - i) : i] == rock[i : i * 2][::-1]:
                return i
        else:
            if rock[0:i] == rock[i : i * 2][::-1]:
                return i


def almost_mirrored(lists1, lists2):
    diff = 0
    for x_list, y_list in zip(lists1, lists2):
        for x, y in zip(x_list, y_list):
            if x != y:
                diff += 1
    return diff == 1


def smudged_mirror_point(rock):
    for i in range(1, len(rock)):
        if i > len(rock) // 2:
            if almost_mirrored(rock[i - (len(rock) - i) : i], rock[i : i * 2][::-1]):
                return i
        else:
            if almost_mirrored(rock[0:i], rock[i : i * 2][::-1]):
                return i


def solver(parsed, part=1):
    mirror_func = mirror_point if part == 1 else smudged_mirror_point
    notes = 0
    for rock in parsed:
        rotated = list(zip(*rock[::-1]))
        notes += mirror_func(rotated) or mirror_func(rock) * 100

    return notes


def solve(input_data):
    parsed = parse(input_data)
    p1 = solver(parsed)
    p2 = solver(parsed, 2)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2023, 13)

    parsed_ex = parse(puzzle.example_data)
    assert solver(parsed_ex) == 405
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solver(parsed)
    assert solver(parsed_ex, 2) == 400
    puzzle.answer_b = solver(parsed, 2)
