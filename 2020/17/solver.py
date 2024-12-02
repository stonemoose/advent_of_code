from copy import deepcopy


def neighours(x, y, z, seats):
    num = -(seats[x][y][z] == "#")
    for i in range(max(0, x - 1), x + 2):
        for j in range(max(0, y - 1), y + 2):
            for k in range(max(0, z - 1), z + 2):
                num += seats[i][j][k] == "#"
    return num


def hyper_neighours(x, y, z, w, seats):
    num = -(seats[x][y][z][w] == "#")
    for i in range(max(0, x - 1), x + 2):
        for j in range(max(0, y - 1), y + 2):
            for k in range(max(0, z - 1), z + 2):
                for l in range(max(0, w - 1), w + 2):
                    num += seats[i][j][k][l] == "#"
    return num


input_len = 8
size = 7 * 2 + input_len
cubes = [[["." for k in range(size)] for j in range(size)] for i in range(size)]
hyper_cubes = [deepcopy(cubes) for w in range(size)]
with open("input") as f:
    z = (size - input_len) // 2
    w = (size - input_len) // 2
    for x, line in enumerate(f.read().strip().split("\n"), z):
        for y, char in enumerate(line, z):
            cubes[x][y][z] = char
            hyper_cubes[x][y][z][w] = char

for i in range(6):
    old_cubes = deepcopy(cubes)
    old_hyper_cubes = deepcopy(hyper_cubes)
    for x in range(1, size - 1):
        for y in range(1, size - 1):
            for z in range(1, size - 1):
                n = neighours(x, y, z, old_cubes)
                if cubes[x][y][z] == "." and n == 3:
                    cubes[x][y][z] = "#"
                elif cubes[x][y][z] == "#" and n not in (2, 3):
                    cubes[x][y][z] = "."
                for w in range(1, size - 1):
                    n = hyper_neighours(x, y, z, w, old_hyper_cubes)
                    if hyper_cubes[x][y][z][w] == "." and n == 3:
                        hyper_cubes[x][y][z][w] = "#"
                    elif hyper_cubes[x][y][z][w] == "#" and n not in (2, 3):
                        hyper_cubes[x][y][z][w] = "."
print(
    "Part 1: ", sum(char == "#" for plane in cubes for line in plane for char in line)
)
print(
    "Part 2: ",
    sum(
        char == "#"
        for cube in hyper_cubes
        for plane in cube
        for line in plane
        for char in line
    ),
)
