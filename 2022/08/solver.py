from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(2022, 8)

input = puzzle.input_data.strip().split("\n")
tree_grid = [[[int(n), False] for n in line] for line in input]


def visible_trees(line):
    highest = -1
    for tree in line:
        if tree[0] > highest:
            highest = tree[0]
            tree[1] = True


for line in tree_grid:
    visible_trees(line)
    visible_trees(line[::-1])
for i in range(len(tree_grid[0])):
    hor_line = [line[i] for line in tree_grid]
    visible_trees(hor_line)
    visible_trees(hor_line[::-1])


part2 = 0
for x in range(len(tree_grid)):
    for y in range(len(tree_grid[0])):
        tree = [0, 0, 0, 0]
        for x2 in range(x + 1, len(tree_grid)):
            tree[0] += 1
            if tree_grid[x][y][0] <= tree_grid[x2][y][0]:
                break
        for x2 in range(x - 1, -1, -1):
            tree[1] += 1
            if tree_grid[x][y][0] <= tree_grid[x2][y][0]:
                break
        for y2 in range(y + 1, len(tree_grid[0])):
            tree[3] += 1
            if tree_grid[x][y][0] <= tree_grid[x][y2][0]:
                break
        for y2 in range(y - 1, -1, -1):
            tree[2] += 1
            if tree_grid[x][y][0] <= tree_grid[x][y2][0]:
                break

        part2 = max(part2, np.prod(tree))

puzzle.answer_a = sum([sum([tree[1] for tree in tree_line]) for tree_line in tree_grid])
puzzle.answer_b = part2
