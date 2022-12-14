from aocd.models import Puzzle


class FallingIntoAbyss(Exception):
    pass


class SourceBlocked(Exception):
    pass


def get_nums(p_from, p_to):
    if p_from[0] > p_to[0] or p_from[1] > p_to[1]:
        p_from, p_to = p_to, p_from
    if p_from[0] != p_to[0]:
        return {(x, p_from[1]) for x in range(p_from[0], p_to[0] + 1)}
    return {(p_from[0], y) for y in range(p_from[1], p_to[1] + 1)}


def fall_sand(x, y, full, bottom):
    if (x, y) in full:
        raise SourceBlocked
    for _ in range(1000):
        if (x, y + 1) not in full:
            y += 1
        elif (x - 1, y + 1) not in full:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in full:
            x += 1
            y += 1
        else:
            return (x, y)
        if bottom and y + 1 == bottom:
            return (x, y)
    raise FallingIntoAbyss


def solve(rocks, bottom=0):
    full = rocks.copy()
    while True:
        try:
            full.add(fall_sand(500, 0, full, bottom))
        except (FallingIntoAbyss, SourceBlocked):
            return len(full) - len(rocks)


puzzle = Puzzle(2022, 14)
input = puzzle.input_data.strip().split("\n")

rocks = set()
for line in input:
    points = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    for i in range(len(points) - 1):
        rocks.update(get_nums(points[i], points[i + 1]))


puzzle.answer_a = solve(rocks)
max_y = max(i[1] for i in rocks)
puzzle.answer_b = solve(rocks, max_y + 2)
