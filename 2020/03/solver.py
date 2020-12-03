import numpy as np


def traverse(right, down, matrix):
    col, row = 0, 0
    sum = 0
    while row < len(matrix):
        sum += input[row][col]
        col += right
        col %= len(matrix[0])
        row += down
    return sum


input = [[char == '#' for char in line] for line in open('input').read().splitlines()]
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print("Part 1:", traverse(3, 1, input))
print("Part 2:", np.prod([traverse(r, d, input) for r, d in slopes]))
