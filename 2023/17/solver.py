from aocd.models import Puzzle
import heapq as hq
import numpy as np


def parse(input_data):
    return np.array(
        [[int(char) for char in line] for line in input_data.strip().split("\n")]
    )


def print_map(parsed):
    for line in parsed:
        print("".join(map(str, line)))


def dijkstra(start, grid, min_moves, max_moves):
    n = len(grid)
    vert_visited = np.full((n, n), False)
    hor_visited = np.full((n, n), False)
    vertical_weights = np.full((n, n), np.inf)
    horizontal_weights = np.full((n, n), np.inf)
    queue = []
    vertical_weights[start] = horizontal_weights[start] = grid[start]
    hq.heappush(queue, (0, "horizontal", start))
    hq.heappush(queue, (0, "vertical", start))

    while queue:
        heat_loss, direction, pos = hq.heappop(queue)
        x, y = pos

        if direction == "horizontal":
            if hor_visited[pos]:
                continue
            hor_visited[pos] = True
            for i in range(min_moves, min(max_moves + 1, y + 1)):
                new_loss = heat_loss + sum(grid[x, y - j] for j in range(1, i + 1))
                if vert_visited[x, y - i]:
                    continue
                if new_loss < vertical_weights[x, y - i]:
                    vertical_weights[x, y - i] = new_loss
                    hq.heappush(queue, (new_loss, "vertical", (x, y - i)))

            for i in range(min_moves, min(max_moves + 1, n - y)):
                new_loss = heat_loss + sum(grid[x, y + j] for j in range(1, i + 1))
                if vert_visited[x, y + i]:
                    continue
                if new_loss < vertical_weights[x, y + i]:
                    vertical_weights[x, y + i] = new_loss
                    hq.heappush(queue, (new_loss, "vertical", (x, y + i)))

        elif direction == "vertical":
            if vert_visited[pos]:
                continue
            vert_visited[pos] = True
            for i in range(min_moves, min(max_moves + 1, x + 1)):
                new_loss = heat_loss + sum(grid[x - j, y] for j in range(1, i + 1))
                if hor_visited[x - i, y]:
                    continue
                if new_loss < horizontal_weights[x - i, y]:
                    horizontal_weights[x - i, y] = new_loss
                    hq.heappush(queue, (new_loss, "horizontal", (x - i, y)))

            for i in range(min_moves, min(max_moves + 1, n - x)):
                new_loss = heat_loss + sum(grid[x + j, y] for j in range(1, i + 1))
                if hor_visited[x + i, y]:
                    continue
                if new_loss < horizontal_weights[x + i, y]:
                    horizontal_weights[x + i, y] = new_loss
                    hq.heappush(queue, (new_loss, "horizontal", (x + i, y)))

    return np.minimum(vertical_weights, horizontal_weights)


def solver(parsed, min_moves=1, max_moves=3):
    start = (0, 0)
    distance_map = dijkstra(start, parsed, min_moves, max_moves)
    return int(distance_map[-1, -1])


def solve(input_data):
    parsed = parse(input_data)
    p1 = solver(parsed)
    p2 = solver(parsed, 4, 10)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2023, 17)

    parsed_ex = parse(puzzle.example_data)
    assert solver(parsed_ex) == 102
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solver(parsed)

    assert solver(parsed_ex, 4, 10) == 94
    parsed = parse(puzzle.input_data)
    puzzle.answer_b = solver(parsed, 4, 10)
