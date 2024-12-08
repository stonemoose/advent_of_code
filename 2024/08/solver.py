import re
from aocd.models import Puzzle
import aoc_functionality.grid_helper as gh
import math


def parse(input_data):
    parsed = []
    for line in input_data.split("\n"):
        parsed.append(list(line))
    return parsed


def helper2(x, y, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                continue
            if i == x and y == j:
                continue

            x_dir = int((i - x) / math.gcd((i - x), (j - y)))
            y_dir = int((j - y) / math.gcd((i - x), (j - y)))

            for n in range(-100, 100):
                next_x = x + n * x_dir
                next_y = y + n * y_dir
                if next_x == i:
                    continue
                if gh.coords_in_grid(next_x, next_y, grid):
                    if grid[next_x][next_y] == grid[i][j]:
                        return True
    return False


def helper(x, y, grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in ".#":
                continue
            if i == x and y == j:
                continue

            next_x = x + 2 * (i - x)
            next_y = y + 2 * (j - y)
            if gh.coords_in_grid(next_x, next_y, grid):
                if grid[next_x][next_y] == grid[i][j]:
                    return True
    return False


def solve(input_data):
    grid = parse(input_data)
    p1 = p2 = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if helper(x, y, grid):
                p1 += 1
            if helper2(x, y, grid):
                p2 += 1

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 8)

    assert solve(puzzle.examples[0].input_data) == (14, 34)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
