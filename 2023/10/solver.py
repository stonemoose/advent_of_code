from aocd.models import Puzzle
from aoc_functionality.util import Color


def parse(input_data):
    parsed = (
        input_data.replace("|", "┃")
        .replace("-", "━")
        .replace("F", "┏")
        .replace("7", "┓")
        .replace("L", "┗")
        .replace("J", "┛")
    )
    parsed = parsed.strip().replace(".", "#").split("\n")
    return parsed


def check_one_side(coords: list, start: tuple[int, int], right=False):
    last_x, last_y = start
    loop_contained = set()
    one = -1 if right else 1
    for x, y in coords:
        if y < last_y:
            loop_contained.add((x + one, y))
            loop_contained.add((x + one, y + 1))
        elif y > last_y:
            loop_contained.add((x - one, y))
            loop_contained.add((x - one, y - 1))
        elif x > last_x:
            loop_contained.add((x, y + one))
            loop_contained.add((x - 1, y + one))
        elif x < last_x:
            loop_contained.add((x, y - one))
            loop_contained.add((x + 1, y - one))
        last_x, last_y = x, y
    return loop_contained


def print_map(visited, enclosed, parsed_data, outside):
    for y in range(len(parsed_data)):
        for x in range(len(parsed_data[0])):
            if (x, y) in visited:
                print(Color.GREEN + parsed_data[y][x], end=Color.END)
            elif (enclosed[y][x] and outside) or (not enclosed[y][x] and not outside):
                print(Color.BOLD + Color.RED + parsed_data[y][x], end=Color.END)
            else:
                print(parsed_data[y][x], end=Color.END)
        print()


def solve(input_data, should_print=False):
    parsed_data = parse(input_data)
    distance = [[0] * len(parsed_data[0]) for _ in range(len(parsed_data))]
    enclosed = [[0] * len(parsed_data[0]) for _ in range(len(parsed_data))]
    loop_contained = set()
    to_visit = []
    visited = []
    start = None
    for y in range(len(parsed_data)):
        for x in range(len(parsed_data[y])):
            if parsed_data[y][x] == "S":
                start = (x, y)
                to_visit.append([x, y])

    while to_visit:
        x, y = to_visit.pop(0)
        visited.append((x, y))
        symbol = parsed_data[y][x]
        if y > 0 and symbol in "S┃┛┗":
            if parsed_data[y - 1][x] in "┃┓┏":
                if (x, y - 1) not in visited:
                    to_visit.append([x, y - 1])
                    distance[y - 1][x] = distance[y][x] + 1

        if y < len(parsed_data) and symbol in "S┃┏┓":
            if parsed_data[y + 1][x] in "┃┛┗":
                if (x, y + 1) not in visited:
                    to_visit.append([x, y + 1])
                    distance[y + 1][x] = distance[y][x] + 1

        if x > 0 and symbol in "S━┛┓":
            if parsed_data[y][x - 1] in "━┏┗":
                if (x - 1, y) not in visited:
                    to_visit.append([x - 1, y])
                    distance[y][x - 1] = distance[y][x] + 1

        if x < len(parsed_data[y]) and symbol in "S━┏┗":
            if parsed_data[y][x + 1] in "━┛┓":
                if (x + 1, y) not in visited:
                    to_visit.append([x + 1, y])
                    distance[y][x + 1] = distance[y][x] + 1

    for right in (True, False):
        loop_contained.update(check_one_side(visited[1 + right :: 2], start, right))

    outside = False
    while loop_contained:
        x, y = loop_contained.pop()
        if not ((0 <= x < len(parsed_data[0])) and (0 <= y < len(parsed_data))):
            outside = True
            continue
        if enclosed[y][x] or (x, y) in visited:
            continue
        enclosed[y][x] = 1
        loop_contained.add((x + 1, y))
        loop_contained.add((x - 1, y))
        loop_contained.add((x, y + 1))
        loop_contained.add((x, y - 1))

    furthest = max([max(line) for line in distance])
    num_enclosed = sum([sum(line) for line in enclosed])
    if outside:
        num_enclosed = (
            len(distance[0]) * len(distance)
            - sum([sum([bool(i) for i in line]) for line in distance])
            - num_enclosed
            - 1  # start
        )
    if should_print:
        print_map(visited, enclosed, parsed_data, outside)
        print(furthest, num_enclosed)
    return furthest, num_enclosed


if __name__ == "__main__":
    puzzle = Puzzle(2023, 10)

    example = """
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
"""

    example3 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
    example2 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""
    if solve(example)[1] != 4:
        quit()
    if solve(example2)[1] != 8:
        quit()
    if solve(example3)[1] != 10:
        quit()
    puzzle.answer_a, puzzle.answer_b = solve(puzzle.parsed, should_print=True)
