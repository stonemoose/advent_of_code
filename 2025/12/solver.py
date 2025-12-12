from aocd.models import Puzzle
from functools import cache
import numpy as np
import copy


def print_progress_bar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=100,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def parse(input_data):
    *shapes, regions = input_data.strip().split("\n\n")
    parsed_shapes = []
    for shape in shapes:
        shape = shape.split("\n")[1:]
        parsed_shapes.append(
            np.array([[int(c == "#") for c in line] for line in shape])
        )
    parsed_regions = []
    for region in regions.split("\n"):
        shape, *quantities = region.split(" ")
        shape = tuple(map(int, shape.strip(":").split("x")))
        quantities = [int(q) for q in quantities]
        parsed_regions.append((shape, quantities))

    return parsed_shapes, parsed_regions


seen = set()


# Hard coded rotational symmetries for my input
def all_rots(shape, i):
    if i == 1:
        yield shape
        yield np.rot90(shape)
    elif i in (2, 3, 4):
        for _ in range(4):
            yield shape
            shape = np.rot90(shape)
    else:
        for _ in range(4):
            yield shape
            shape = np.rot90(shape)
        shape = np.fliplr(shape)
        for _ in range(4):
            yield shape
            shape = np.rot90(shape)


def can_fit(space, quantities, shapes, last=-1):
    global seen
    if sum(quantities) == 0:
        return True
    for i in [1, 3, 2, 4, 5, 0]:
        if quantities[i]:
            if i != last:
                seen = set()
            shape = shapes[i]
            for x in range(space.shape[0] - 2):
                for y in range(space.shape[1] - 2):
                    if (x, y) in seen:
                        continue
                    seen.add((x, y))
                    for shape in all_rots(shape, i):
                        negation = space[x : x + 3, y : y + 3] - shape
                        if np.min(negation) >= 0:
                            next_space = copy.deepcopy(space)
                            next_space[x : x + 3, y : y + 3] = negation

                            next_quant = copy.deepcopy(quantities)
                            next_quant[i] -= 1
                            if can_fit(next_space, next_quant, shapes, i):
                                return True
            return False
    return False


def solve(input_data):
    p1 = p2 = 0
    shapes, regions = parse(input_data)
    i = 0
    for shape, quantities in regions:
        i += 1
        print_progress_bar(i, len(regions))
        space = np.ones(shape)
        ans = can_fit(space, quantities, shapes)
        p1 += ans
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 12)
    e1, e2 = solve(puzzle.examples[0].input_data)
    if e1 != 2:
        print("test failed")
        quit()
    print(e1, e2)
    p1, p2 = solve(puzzle.input_data)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
