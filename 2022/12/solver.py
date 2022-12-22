from aocd.models import Puzzle

puzzle = Puzzle(2022, 12)

grid = puzzle.input_data.strip().split("\n")


def get_neighbours(x, y, max_x, max_y):
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if x < max_x:
        neighbours.append((x + 1, y))
    if y < max_y:
        neighbours.append((x, y + 1))
    return neighbours


def height_diff_ok(grid, x, y, x2, y2):
    if grid[x][y] == "S":
        current = "a"
    else:
        current = grid[x][y]
    if grid[x2][y2] == "E":
        going_to = "z"
    else:
        going_to = grid[x2][y2]
    return ord(going_to) - ord(current) <= 1


def bfs(grid, start_x, start_y):
    next_stack = {(start_x, start_y)}
    seen = set()
    largest_x = len(grid) - 1
    largest_y = len(grid[0]) - 1
    counter = 0
    while next_stack:
        stack = next_stack
        next_stack = set()
        while stack:
            x, y = stack.pop()
            if grid[x][y] == "E":
                return counter
            seen.add((x, y))
            for x2, y2 in get_neighbours(x, y, largest_x, largest_y):
                if (x2, y2) not in seen and height_diff_ok(grid, x, y, x2, y2):
                    next_stack.add((x2, y2))
        counter += 1


for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "S":
            puzzle.answer_a = bfs(grid, x, y)

best = int(puzzle.answer_a)

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "a":
            if bfs(grid, x, y):
                best = min(best, bfs(grid, x, y))
puzzle.answer_b = best
