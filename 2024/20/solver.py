from aocd.models import Puzzle
from aoc_functionality.util import profile
import math
from collections import defaultdict
import aoc_functionality.grid_helper as gh


def parse(input_data):
    lines = input_data.split("\n")
    return [list(l) for l in lines]


def get_distances(grid, start):
    visited = set()
    scores = defaultdict(lambda: math.inf)
    scores[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        visited.add(current)

        for next_coord in gh.get_neighbours(
            current[0], current[1], len(grid), len(grid[0])
        ):
            if grid[next_coord[0]][next_coord[1]] and not next_coord in visited:
                queue.append(next_coord)
                visited.add(next_coord)
                scores[next_coord] = scores[current] + 1
    return scores


def get_cheats(grid, start, scores, max_steps):
    visited = set()
    cheat_scores = defaultdict(int)
    queue = [(0, start)]
    max_x = len(grid)
    max_y = len(grid[0])
    while queue:
        steps, current = queue.pop(0)
        if grid[current[0]][current[1]]:
            cheat_scores[current] = scores[current] - scores[start] - steps

        if steps >= max_steps:
            continue

        for neighbour in gh.get_neighbours(current[0], current[1], max_x, max_y):
            if not neighbour in visited:
                queue.append((steps + 1, neighbour))
                visited.add(neighbour)
    return cheat_scores


def get_all_cheats(grid, scores, max_steps):

    cheat_dict = defaultdict(int)

    for x, line in enumerate(grid[1:-1], 1):
        for y, path in enumerate(line[1:-1], 1):
            if path:
                cheats = get_cheats(grid, (x, y), scores, max_steps)
                for val in cheats.values():
                    cheat_dict[val] += 1

    return cheat_dict


def solve(input_data):
    str_maze = parse(input_data)
    for i, line in enumerate(str_maze):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
    maze = [[c != "#" for c in line] for line in str_maze]
    p1 = p2 = 0
    scores = get_distances(maze, start)
    short_cheats = get_all_cheats(maze, scores, 2)
    long_cheats = get_all_cheats(maze, scores, 20)
    p1 = sum(val for cheat, val in short_cheats.items() if cheat >= 100)
    p2 = sum(val for cheat, val in long_cheats.items() if cheat >= 100)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 20)
    p1, p2 = profile(solve, puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
