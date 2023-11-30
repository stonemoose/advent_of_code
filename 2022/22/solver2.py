from aocd.models import Puzzle
import re


def turn(x, y, dir, turning, tile_size):
    tile_size -= 1
    if turning == 0:
        return x, y, dir
    if turning == 1:
        return y, tile_size - x, (dir + 1) % 4
    if turning == 2:
        return tile_size - x, tile_size - y, (dir + 2) % 4
    if turning == 3:
        return tile_size - y, x, (dir + 3) % 4


class Tile:
    def __init__(self, grid, left_corner=(1, 1)):
        self.left_corner = left_corner
        self.grid = grid
        self.size = len(grid)

    def set_neighbours(self, neighbours):
        self.right = neighbours[0]
        self.down = neighbours[1]
        self.left = neighbours[2]
        self.up = neighbours[3]

    def move_right(self, x, y, dir=0):
        assert dir == 0
        if y < self.size - 1:
            if self.grid[x][y + 1] == ".":
                return self, x, y + 1, dir
            if self.grid[x][y + 1] == "#":
                return self, x, y, dir
        else:
            right, turning = self.right
            new_x, new_y, new_dir = turn(x, 0, dir, turning, self.size)
            if right.grid[new_x][new_y] == "#":
                return self, x, y, dir
            if right.grid[new_x][new_y] == ".":
                return right, new_x, new_y, new_dir

    def move_left(self, x, y, dir=2):
        if y > 0:
            if self.grid[x][y - 1] == ".":
                return self, x, y - 1, dir
            if self.grid[x][y - 1] == "#":
                return self, x, y, dir
        else:
            left, turning = self.left
            new_x, new_y, new_dir = turn(x, self.size - 1, dir, turning, self.size)
            if left.grid[new_x][new_y] == "#":
                return self, x, y, dir
            if left.grid[new_x][new_y] == ".":
                return left, new_x, new_y, new_dir

    def move_down(self, x, y, dir=1):
        if x < self.size - 1:
            if self.grid[x + 1][y] == ".":
                return self, x + 1, y, dir
            if self.grid[x + 1][y] == "#":
                return self, x, y, dir
        else:
            down, turning = self.down
            new_x, new_y, new_dir = turn(0, y, dir, turning, self.size)
            if down.grid[new_x][new_y] == "#":
                return self, x, y, dir
            if down.grid[new_x][new_y] == ".":
                return down, new_x, new_y, new_dir

    def move_up(self, x, y, dir=3):
        if x > 0:
            if self.grid[x - 1][y] == ".":
                return self, x - 1, y, dir
            if self.grid[x - 1][y] == "#":
                return self, x, y, dir
        else:
            up, turning = self.up
            new_x, new_y, new_dir = turn(self.size - 1, y, dir, turning, self.size)
            if up.grid[new_x][new_y] == "#":
                return self, x, y, dir
            if up.grid[new_x][new_y] == ".":
                return up, new_x, new_y, new_dir

    def get_pos(self, x, y):
        return x + self.left_corner[0], y + self.left_corner[1]


def make_tiles(tile_data, length):
    tile_grid = []
    down_parts = [
        (tile_data[i : i + length], i + 1) for i in range(0, len(tile_data), length)
    ]
    for line_group, x in down_parts:
        tile_data = [[y + 1] for y in range(0, len(line_group[0]), length)]
        for line in line_group:
            line_chunks = [line[i : i + length] for i in range(0, len(line), length)]
            for k in range(len(line_chunks)):
                if line_chunks[k][0] == " ":
                    continue
                tile_data[k].append(line_chunks[k])
        tile_grid += [Tile(board, (x, y)) for y, *board in tile_data if board]
    return tile_grid


def solve(start_tile, moves):
    dir = 0
    pos = [0, 0]
    tile = start_tile
    for move in moves:
        if move == "L":
            dir = (dir - 1) % 4
        elif move == "R":
            dir = (dir + 1) % 4
        else:
            for _ in range(int(move)):
                if dir == 0:
                    tile, *pos, dir = tile.move_right(*pos)
                elif dir == 1:
                    tile, *pos, dir = tile.move_down(*pos)
                elif dir == 2:
                    tile, *pos, dir = tile.move_left(*pos)
                elif dir == 3:
                    tile, *pos, dir = tile.move_up(*pos)
    row, column = tile.get_pos(*pos)
    return row * 1000 + column * 4 + dir


def example(puzzle):
    tile_neighbours = {
        0: (0, 3, 0, 4),
        1: (2, 1, 3, 1),
        2: (3, 2, 1, 2),
        3: (1, 4, 2, 0),
        4: (5, 0, 5, 3),
        5: (4, 5, 4, 5),
    }
    input_data = puzzle.example_data.strip("\n").split("\n\n")

    tiles = make_tiles(input_data[0].split("\n"), 4)
    for n, tile in enumerate(tiles):
        tile.set_neighbours([(tiles[i], 0) for i in tile_neighbours[n]])

    moves = re.findall("\d+|\D", input_data[1])
    return solve(tiles[0], moves)


"""
.01
.2.
34.
5..   
"""


def part1(puzzle):
    tile_neighbours = {
        0: (1, 2, 1, 4),
        1: (0, 1, 0, 1),
        2: (2, 4, 2, 0),
        3: (4, 5, 4, 5),
        4: (3, 0, 3, 2),
        5: (5, 3, 5, 3),
    }
    input_data = puzzle.input_data.strip("\n").split("\n\n")

    tiles = make_tiles(input_data[0].split("\n"), 50)
    for n, tile in enumerate(tiles):
        tile.set_neighbours([(tiles[i], 0) for i in tile_neighbours[n]])

    input_data[1] = ""
    moves = re.findall("\d+|\D", input_data[1])
    return solve(tiles[0], moves)


def part2(puzzle):
    x = 0
    tile_neighbours = {
        0: ((1, 0), (2, 0), (3, 2), (5, 1)),
        1: ((4, 2), (2, 1), (0, 0), (5, 0)),
        2: ((1, 3), (4, 0), (3, 3), (0, 0)),
        3: ((4, 0), (5, 0), (0, 2), (2, 1)),
        4: ((1, 2), (5, 1), (3, 0), (2, 0)),
        5: ((4, 3), (1, 0), (0, 3), (3, 0)),
    }
    input_data = puzzle.input_data.strip("\n").split("\n\n")

    tiles = make_tiles(input_data[0].split("\n"), 50)
    for n, tile in enumerate(tiles):
        tile.set_neighbours([(tiles[i[0]], i[1]) for i in tile_neighbours[n]])

    moves = re.findall("\d+|\D", input_data[1])
    return solve(tiles[0], moves)


puzzle = Puzzle(2022, 22)

print(example(puzzle))
print(part1(puzzle))
print(part2(puzzle))
