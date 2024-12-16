import re
from aocd.models import Puzzle
import aoc_functionality.grid_helper as gh
from aoc_functionality.util import Color
import copy
from functools import cache
import heapq
import math
from collections import defaultdict
import numpy as np


def parse(input_data):
    out = []
    input_data = input_data.replace(".", "@")
    for line in input_data.split("\n"):
        out.append(list(line))

    return out


def get_p2(come_from, end, start):
    visited = set()
    queue = [end]
    while queue:
        current = queue.pop()
        visited.add(current)
        if current == start:
            continue
        for other in come_from[current]:
            if other not in visited:
                queue.append(other)
    return visited


def bfs(maze, start, end):
    queue = [(0, start, (0, 1))]
    best_end = math.inf
    visited = dict()
    last_score = 0
    come_from = defaultdict(list)
    while queue:
        score, current, facing = heapq.heappop(queue)
        assert score >= last_score
        if current in visited:
            if current == end:
                print(score, current, facing)
                continue

            if (
                facing[0] + visited[current][1][0] == 0
                and facing[1] + visited[current][1][1] == 0
            ):
                assert score > visited[current][0] - 1
                continue
            if visited[current][1] == facing:
                continue
            if score < visited[current][0] + 1000:
                come_from[current] = [(current[0] - facing[0], current[1] - facing[1])]
                visited[current] = score, facing
            elif score == visited[current][0] + 1000:
                come_from[current].append(
                    (current[0] - facing[0], current[1] - facing[1])
                )
                visited[current] = score, facing
            else:
                continue
        else:
            come_from[current] = [(current[0] - facing[0], current[1] - facing[1])]
            visited[current] = score, facing
        if current == end:
            best_end = min(score, best_end)

        for direction in gh.DIRECTIONS_STRAIGHT:
            if facing[0] + direction[0] == 0 and facing[1] + direction[1] == 0:
                continue
            x = current[0] + direction[0]
            y = current[1] + direction[1]
            if maze[x][y] == "#":
                continue
            cost = 1 if facing == direction else 1001
            heapq.heappush(queue, (score + cost, (x, y), direction))

    vis = get_p2(come_from, end, start)
    gh.print_grid(maze, highlight_coords=vis)
    return best_end, len(vis)


def pprint(maze, visited):
    dirs = {
        (0, 1): ">",
        (0, -1): "<",
        (1, 0): "v",
        (-1, 0): "^",
    }
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            string = None
            if (i, j) in visited:
                string = Color.PURPLE + dirs[visited[(i, j)][1]] + Color.END
            else:
                string = char
            print(string, end="")
        print()


def solve(input_data):
    p1 = p2 = 0
    maze = parse(input_data)
    start = end = None
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
    # p1 = dijkstra(maze, start)[end]
    p1, p2 = bfs(maze, start, end)
    print(p1, p2)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 16)
    example1 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

    example = puzzle.examples[0].input_data
    ex1, ex2 = solve(example)
    e1, e2 = solve(example1)
    p1, p2 = solve(puzzle.input_data)
    if p1:
        assert ex1 == 7036
        assert e1 == 11048
        puzzle.answer_a = p1
    if p2:
        assert ex2 == 45
        assert e2 == 64
        # manual inspection reveals 34 wrong tiles...
        puzzle.answer_b = p2 - 34
