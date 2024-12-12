from aocd.models import Puzzle
import aoc_functionality.grid_helper as gh
from aoc_functionality.util import profile


def parse(input_data):
    out = []
    for line in input_data.split("\n"):
        out.append(list("." + line + "."))
    out.append(["."] * len(out[0]))
    out.insert(0, ["."] * len(out[0]))
    return out


def get_min_max(garden_plots):
    min_x = min_y = max_x = max_y = 0
    for plot in garden_plots:
        min_x = min(min_x, plot[0])
        min_y = min(min_y, plot[1])
        max_x = max(max_x, plot[0])
        max_y = max(max_y, plot[1])
    return min_x, max_x, min_y, max_y


def count_edges(garden_plots):
    min_x, max_x, min_y, max_y = get_min_max(garden_plots)
    corners = 0
    for x in range(min_x - 1, max_x + 1):
        for y in range(min_y - 1, max_y + 1):
            nw = (x, y) in garden_plots
            ne = (x, y + 1) in garden_plots
            sw = (x + 1, y) in garden_plots
            se = (x + 1, y + 1) in garden_plots
            in_garden = sum((nw, ne, sw, se))
            if in_garden == 3:
                corners += 1
            elif in_garden == 1:
                corners += 1
            elif (nw and se) and not (ne and sw) or not (nw and se) and (ne and sw):
                corners += 2
    return corners


def garden_region(x, y, grid, visited):
    queue = [(x, y)]
    garden_plots = {(x, y)}
    max_x = len(grid)
    max_y = len(grid[0])
    perim = 0
    while queue:
        current = queue.pop(0)
        visited.add(current)
        neighbours = 0
        for other in gh.get_neighbours(current[0], current[1], max_x, max_y):
            if grid[other[0]][other[1]] != grid[current[0]][current[1]]:
                continue
            neighbours += 1
            garden_plots.add(current)
            if other not in visited:
                visited.add(other)
                queue.append(other)
        perim += 4 - neighbours

    area = len(garden_plots)
    edges = count_edges(garden_plots)
    return area, perim, edges


def solve(input_data):
    grid = parse(input_data)
    p1 = p2 = 0

    visited = set()
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if (x, y) in visited:
                continue
            area, perim, edges = garden_region(x, y, grid, visited)
            p1 += area * perim
            p2 += area * edges

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 12)
    p1, p2 = profile(solve, puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
