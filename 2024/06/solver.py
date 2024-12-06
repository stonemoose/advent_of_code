import re
import copy
from aocd.models import Puzzle
import aoc_functionality.grid_helper as gh


def parse(input_data):
    return [list(line) for line in input_data.split("\n")]


def guard_path(grid, pos, direction):
    turn_right = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }

    visited = {pos: [direction]}
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    loop = False

    while gh.coords_in_grid(*next_pos, grid):
        if grid[next_pos[0]][next_pos[1]] == "#":
            direction = turn_right[direction]
            next_pos = (pos[0] + direction[0], pos[1] + direction[1])
            continue
        if next_pos in visited:
            if direction in visited[next_pos]:
                loop = True
                break
            visited[next_pos].append(direction)
        else:
            visited[next_pos] = [direction]
        pos = next_pos
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

    return visited, loop


def solve(input_data):
    grid = parse(input_data)
    p1 = p2 = 0

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "^":
                pos = (i, j)
                direction = (-1, 0)

    visited = guard_path(grid, pos, direction)[0]
    p1 = len(visited)

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if not ((i, j) in visited and char == "."):
                continue
            grid[i][j] = "#"
            start_dir = visited[(i, j)][0]
            start_pos = (i - start_dir[0], j - start_dir[1])
            p2 += guard_path(grid, start_pos, start_dir)[1]
            grid[i][j] = "."

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 6)
    for example in puzzle.examples:
        ex1, ex2 = solve(example.input_data)
        assert ex1 == 41
        assert ex2 == 6
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
