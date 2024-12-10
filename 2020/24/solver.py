from copy import deepcopy
import re

flipped = set()


def hex_neighours(x, y, floor):
    neighbour_dirs = ((1, 1), (2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1))
    num = 0
    for i, j in neighbour_dirs:
        try:
            num += floor[x + j][y + i]
        except IndexError:
            pass
    return num


def coordinate(se, nw, ne, sw, w, e):
    s = se + sw
    n = ne + nw
    e = se + ne + 2 * e
    w = nw + sw + 2 * w
    return (s - n, e - w)


def solve(input_data):
    for line in input_data.split("\n"):
        oline = line
        se = len(re.findall("se", line))
        line = line.replace("se", "")
        nw = len(re.findall("nw", line))
        line = line.replace("nw", "")
        ne = len(re.findall("ne", line))
        line = line.replace("ne", "")
        sw = len(re.findall("sw", line))
        line = line.replace("sw", "")
        e = len(re.findall("e", line))
        line = line.replace("e", "")
        w = len(re.findall("w", line))
        tile = coordinate(se, nw, ne, sw, w, e)
        if tile not in flipped:
            flipped.add(tile)
        else:
            flipped.remove(tile)

    p1 = len(flipped)

    size = 300
    floor = [[0] * size for i in range(size)]
    mid = size // 2

    for x, y in flipped:
        floor[mid + x][mid + y] = 1

    for i in range(1, 101):
        old_floor = deepcopy(floor)
        for x in range(size):
            for y in range(size):
                n = hex_neighours(x, y, old_floor)
                if old_floor[x][y] and (n == 0 or n > 2):
                    floor[x][y] = 0
                elif not old_floor[x][y] and n == 2:
                    floor[x][y] = 1

    p2 = sum(tile for line in floor for tile in line)

    return p1, p2
