from aocd.models import Puzzle


def parse(input_data):
    parsed = []
    for line in input_data.strip().split():
        parsed.append(tuple(int(n) for n in line.split(",")))
    return parsed


def rectangle_size(start, end):
    return (abs(start[0] - end[0]) + 1) * (abs(start[1] - end[1]) + 1)


def crosses_line(line, start, end):
    square = [start, (start[0], end[1]), end, (end[0], start[1])]
    edges = list(zip(square, square[1:] + [square[0]]))

    if line[0][0] == line[1][0]:
        return any(
            min(line[0][1], line[1][1]) <= edge[0][1] <= max(line[0][1], line[1][1])
            and min(edge[0][0], edge[1][0]) < line[0][0] < max(edge[0][0], edge[1][0])
            for edge in edges
        )
    return any(
        min(line[0][0], line[1][0]) <= edge[0][0] <= max(line[0][0], line[1][0])
        and min(edge[0][1], edge[1][1]) < line[0][1] < max(edge[0][1], edge[1][1])
        for edge in edges
    )


def inside(point, start, end):

    if point == start or point == end:
        return False
    x_inside = start[0] < point[0] < end[0] or end[0] < point[0] < start[0]
    y_inside = start[1] < point[1] < end[1] or end[1] < point[1] < start[1]
    return x_inside and y_inside


def solve(input_data):
    p1 = p2 = 0
    points = parse(input_data)
    lines = [(start, end) for start, end in zip(points, points[1:] + [points[0]])]

    all_rectangles = []
    # O(n^2), n = punkter for å lage rektangler
    for i, start in enumerate(points, 1):
        for end in points[i:]:
            all_rectangles.append((rectangle_size(start, end), start, end))
    all_rectangles.sort(reverse=True)
    p1 = all_rectangles[0][0]

    for size, start, end in all_rectangles:
        if not any(crosses_line(line, start, end) for line in lines):
            p2 = size
            break

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 9)
    p1, p2 = solve(puzzle.input_data)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
