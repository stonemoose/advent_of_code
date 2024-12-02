import math


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


def bfs(grid, start_x, start_y):
    stack = {(start_x, start_y)}
    seen = set()
    largest_x = len(grid) - 1
    largest_y = len(grid[0]) - 1
    while stack:
        x, y = stack.pop()
        seen.add((x, y))
        for x2, y2 in get_neighbours(x, y, largest_x, largest_y):
            if (x2, y2) not in seen and grid[x2][y2] != 9:
                stack.add((x2, y2))
    return seen


if __name__ == "__main__":

    with open("input") as f:
        height_map = [[int(n) for n in line.strip()] for line in f.readlines()]

    part1 = 0
    part2 = []
    largest_x = len(height_map) - 1
    largest_y = len(height_map[0]) - 1

    for x in range(len(height_map)):
        for y in range(len(height_map[0])):
            for x2, y2 in get_neighbours(x, y, largest_x, largest_y):
                if height_map[x][y] >= height_map[x2][y2]:
                    break
            else:
                part1 += height_map[x][y] + 1
                part2.append(len(bfs(height_map, x, y)))

    print(f"Part 1: {part1}")
    print(f"Part 2: {math.prod(sorted(part2)[-3:])}")
