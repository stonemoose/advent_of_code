import copy
from aocd.models import Puzzle
from aoc_functionality import grid_helper as gh


def parse(input_data):
    lines = input_data.strip().split("\n")
    return [[char == "#" for char in line] for line in lines]


def next_state(grid):
    next_grid = copy.deepcopy(grid)
    for x in range(len(grid)):
        for y in range(len(grid)):
            neighbours_on = 0
            for n_x, n_y in gh.get_neighbours(
                x, y, len(grid), len(grid), diagonal=True
            ):
                neighbours_on += grid[n_x][n_y]
            if grid[x][y]:
                next_grid[x][y] = neighbours_on in (2, 3)
            else:
                next_grid[x][y] = neighbours_on == 3
    return next_grid


def run_life(grid, iterations, locked_corners=False):
    for _ in range(iterations):
        if locked_corners:
            grid[0][0] = grid[0][-1] = grid[-1][0] = grid[-1][-1] = True
        grid = next_state(grid)
    if locked_corners:
        grid[0][0] = grid[0][-1] = grid[-1][0] = grid[-1][-1] = True
    return grid


def sum_grid(grid):
    return sum([sum(line) for line in grid])


def solve(input_data, iterations=100):
    grid = parse(input_data)
    p1 = sum_grid(run_life(copy.deepcopy(grid), iterations=iterations))

    grid = parse(input_data)
    p2 = sum_grid(run_life(grid, iterations=iterations, locked_corners=True))

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2015, 18)
    ex1, ex2 = solve(puzzle.examples[0].input_data, iterations=4)
    assert ex1 == 4
    assert ex2 == 14

    grid = parse(puzzle.input_data)
    puzzle.answer_a = sum_grid(run_life(grid, iterations=100))

    grid = parse(puzzle.input_data)
    puzzle.answer_b = sum_grid(run_life(grid, iterations=100, locked_corners=True))
