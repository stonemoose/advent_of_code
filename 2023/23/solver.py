from copy import deepcopy
from aocd.models import Puzzle
import numpy as np


def get_neighbours(x, y, max_x, max_y, grid):
    if x > 0 and not grid[x - 1, y] == "v":
        yield x - 1, y
    if y > 0 and not grid[x, y - 1] == ">":
        yield x, y - 1

    if x < max_x - 1 and not grid[x + 1, y] == "^":
        yield x + 1, y
    if y < max_y - 1 and not grid[x, y + 1] == "<":
        yield x, y + 1


def get_all_neighbours(x, y):
    yield (x - 1, y)
    yield (x, y - 1)
    yield (x + 1, y)
    yield (x, y + 1)


def parse(input_data):
    grid = np.array(
        [list(line) for line in input_data.strip().split("\n")], dtype=object
    )
    for x in range(1, len(grid) - 1):
        for y in range(len(grid[0]) - 1):
            if grid[x, y] == "." and not any(
                (grid[x2, y2] == "." for x2, y2 in get_all_neighbours(x, y))
            ):
                left = grid[x, y - 1]
                right = grid[x, y + 1]
                up = grid[x - 1, y]
                down = grid[x + 1, y]
                grid[x, y] = Intersection(left, right, up, down, (x, y))
    return grid


class Intersection:
    def __init__(self, left, right, up, down, coords):
        self.coords = coords
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.next_intersections = {}
        self.all_next = {}
        self.visited = False
        self.end_dist = 0

    def __hash__(self):
        return id(self)

    def get_next_step(self, x, y):
        if self.left == "<":
            yield x, y - 1
        if self.right == ">":
            yield x, y + 1
        if self.up == "^":
            yield x - 1, y
        if self.down == "v":
            yield x + 1, y

    def add_intersection(self, intersection, dist):
        self.next_intersections[intersection] = dist
        self.all_next[intersection] = dist
        intersection.all_next[self] = dist

    def longest_way_to_end(self):
        max_distance = self.end_dist
        for slope, dist in self.next_intersections.items():
            max_distance = max(max_distance, slope.longest_way_to_end() + dist)
        return max_distance

    def longest_unrestrained_way_to_end(self, visited=set()):
        visited = visited.copy()
        visited.add(self)
        if self.end_dist:
            return self.end_dist

        max_distance = self.end_dist
        for intersection, dist in self.all_next.items():
            if not intersection in visited:
                distance = intersection.longest_unrestrained_way_to_end(visited) + dist
                if distance > max_distance:
                    max_distance = distance
        return max_distance

    def __str__(self):
        return "+"

    def __eq__(self, other):
        return str(self) == other


def bfs(grid, start_x, start_y):
    next_nodes = set()
    visited = set()
    start = grid[start_x, start_y]
    next_stack = set(start.get_next_step(start_x, start_y))
    visited = {(start_x, start_y)}
    counter = 1

    max_x = len(grid)
    max_y = len(grid[0])

    while next_stack:
        stack = next_stack
        next_stack = set()
        while stack:
            x, y = stack.pop()
            position = grid[x, y]
            if isinstance(position, Intersection):
                start.add_intersection(position, counter)
                next_nodes.add((x, y))
                continue
            visited.add((x, y))
            for x2, y2 in get_neighbours(x, y, max_x, max_y, grid):
                if (x2, y2) not in visited and grid[x2, y2] != "#":
                    if x2 == max_x - 1 or y2 == max_y - 1:
                        start.end_dist = counter + 1
                        continue
                    next_stack.add((x2, y2))
        counter += 1
    return next_nodes


def connect_intersections(grid, start):
    for x, y in bfs(grid, *start):
        connect_intersections(grid, (x, y))


def solve(input_data):
    parsed = parse(input_data)
    start = (0, int(np.where(parsed[0] == ".")[0]))
    parsed[start] = Intersection(up="#", left="#", right="#", down="v", coords=start)
    connect_intersections(parsed, start)
    return (
        parsed[start].longest_way_to_end(),
        parsed[start].longest_unrestrained_way_to_end(),
    )


def print_map(parsed):
    for line in parsed:
        print("".join(map(str, line)))


if __name__ == "__main__":
    puzzle = Puzzle(2023, 23)

    assert solve(puzzle.examples[0].input_data) == (94, 154)
    puzzle.answer_a, puzzle.answer_b = solve(puzzle.input_data)
