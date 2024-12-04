from aocd.models import Puzzle
import aoc_functionality.grid_helper as gh


def parse(input_data):
    out = []
    for line in input_data.strip().split("\n"):
        out.append(line)
    return out


def word_search(x, y, grid, word="XMAS", direction=None):
    if word == "":
        return 1
    if not gh.coords_in_grid(x, y, grid):
        return 0
    if grid[x][y] != word[0]:
        return 0
    if direction:
        nx = x + direction[0]
        ny = y + direction[1]
        return word_search(nx, ny, grid, word[1:], direction)

    hits = 0
    for d in gh.DIRECTIONS_ALL:
        if word_search(x + d[0], y + d[1], grid, word[1:], d):
            hits += 1
    return hits


def x_mas(square):
    if len(square) < 3 or len(square[0]) < 3:
        return 0
    diag1 = "".join(square[i][i] for i in range(len(square)))
    diag2 = "".join(square[i][-1 - i] for i in range(len(square[0])))
    if diag1 in ("MAS", "SAM") and diag2 in ("MAS", "SAM"):
        return 1
    return 0


def solve(parsed):
    p1 = p2 = 0
    for x in range(len(parsed)):
        for y in range(len(parsed[0])):
            p1 += word_search(x, y, parsed)
            square = [line[y : y + 3] for line in parsed[x : x + 3]]
            p2 += x_mas(square)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 4)
    p1, p2 = solve(parse(puzzle.input_data))
    print(p1, p2)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
