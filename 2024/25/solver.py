from aocd.models import Puzzle
import re


def parse(input_data):
    locks = []
    keys = []
    for schematic in input_data.split("\n\n"):
        heights = []
        for column in zip(*schematic.split("\n")):
            heights.append(len(re.findall(r"#+", "".join(column))[0]) - 1)
        if schematic[0][0] == "#":
            locks.append(heights)
        elif schematic[0][0] == ".":
            keys.append(heights)
        else:
            raise Exception
    return locks, keys


def test(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True


def solve(input_data):
    p1 = p2 = 0

    keys, locks = parse(input_data)
    keys = sorted(keys)
    locks = sorted(locks, reverse=True)

    print(len(keys))
    print(len(locks))

    for key in keys:
        for lock in locks:
            p1 += test(key, lock)

    print(p1)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 25)
    man_ex = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".strip()
    e1, e2 = solve(man_ex)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
