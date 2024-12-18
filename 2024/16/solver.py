from aocd.models import Puzzle
import heapq as hq
from collections import defaultdict
import math


def parse(input_data):
    out = []
    for line in input_data.split("\n"):
        out.append(list(line))
    return out


def dijkstra(maze, start):
    directions = {
        0: (0, 1),  # east
        1: (1, 0),  # south
        2: (0, -1),  # west
        3: (-1, 0),  # north
    }

    visited = defaultdict(lambda: [False] * 4)
    scores = defaultdict(lambda: {d: math.inf for d in directions})
    parents = defaultdict(lambda: {d: set() for d in directions})
    scores[start][0] = 0
    queue = [(0, start, 0)]
    while queue:
        score, current, facing = hq.heappop(queue)
        visited[current][facing] = True

        forwards = (
            current[0] + directions[facing][0],
            current[1] + directions[facing][1],
        )
        next_score = score + 1
        if maze[forwards[0]][forwards[1]]:
            if not visited[forwards][facing]:
                if next_score < scores[forwards][facing]:
                    parents[forwards][facing] = {(current, facing)}
                    scores[forwards][facing] = next_score
                    hq.heappush(queue, (next_score, forwards, facing))
                if next_score == scores[forwards][facing]:
                    parents[forwards][facing].add((current, facing))

        for turn in (-1, 1):
            turned = (facing + turn) % 4
            turned_score = score + 1000
            if not visited[current][turned]:
                if turned_score <= scores[current][turned]:
                    parents[current][turned].add((current, facing))
                    scores[current][turned] = turned_score
                    hq.heappush(queue, (turned_score, current, turned))
    return scores, parents


def get_all_paths(scores, parents, end):
    queue = []
    end_score = math.inf
    for end_direction, score in scores[end].items():
        if score < end_score:
            queue = [(end, end_direction)]
        elif score == end_score:
            queue.append((end, end_direction))

    visited = set()
    while queue:
        current, direction = queue.pop(0)
        visited.add(current)
        for parent_direction in parents[current][direction]:
            queue.append(parent_direction)
    return visited


def solve(input_data):
    p1 = p2 = 0
    str_maze = parse(input_data)
    start = end = None
    for i, line in enumerate(str_maze):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
    maze = [[c != "#" for c in line] for line in str_maze]

    scores, parents = dijkstra(maze, start)
    p1 = min(scores[end].values())
    p2 = len(get_all_paths(scores, parents, end))
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 16)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
