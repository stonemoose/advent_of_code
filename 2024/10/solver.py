from aocd.models import Puzzle
from collections import defaultdict
import aoc_functionality.grid_helper as gh


def parse(input_data):
    data = []
    for line in input_data.split("\n"):
        data.append([int(num) for num in line])

    return data


def trailhead_score(heights, start, parents):
    queue = [start]
    visited = {start}
    max_x = len(heights)
    max_y = len(heights[0])
    while queue:
        current = queue.pop(0)
        visited.add(current)
        for other in gh.get_neighbours(current[0], current[1], max_x, max_y):
            if heights[other[0]][other[1]] != heights[current[0]][current[1]] + 1:
                continue
            parents[other].add(current)
            if other not in visited:
                visited.add(other)
                queue.append(other)
    return sum(heights[v[0]][v[1]] == 9 for v in visited)


def distinct_trails(parents, start):
    ways = parents[start]
    if not ways:
        return 1
    return sum(distinct_trails(parents, child) for child in ways)


def total_trail_rating(grid, parents):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 9:
                ways = parents[(i, j)]
                if not ways:
                    continue
                count += distinct_trails(parents, (i, j))
    return count


def solve(input_data):
    grid = parse(input_data)
    p1 = p2 = 0

    parents = defaultdict(set)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                p1 += trailhead_score(grid, (i, j), parents)
    p2 = total_trail_rating(grid, parents)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 10)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
