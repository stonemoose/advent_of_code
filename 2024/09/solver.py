from aocd.models import Puzzle

from aoc_functionality.util import profile


def parse(input_data):
    file_num = 0
    files = []
    free_space = []
    space = False
    for num in input_data:
        if space:
            free_space.append((int(num)))
        else:
            files.append((int(num), file_num))
            file_num += 1
        space = not space

    free_space.append(9)
    return files, free_space


def part1(files, free_space):
    filled_space = [[] for _ in range(len(free_space))]
    space_index = 0

    size, file_num = files.pop()
    space = free_space[space_index]
    while space_index < (len(files) - 1):
        if size == 0:
            size, file_num = files.pop()
        if space == 0:
            space_index += 1
            space = free_space[space_index]

        if size <= space:
            filled_space[space_index].append((size, file_num))
            space -= size
            size = 0
        else:
            filled_space[space_index].append((space, file_num))
            size -= space
            space = 0
    if size:
        files.append((size, file_num))

    out = []
    for i in range(len(files)):
        out.append(files[i])
        for j in range(len(filled_space[i])):
            out.append(filled_space[i][j])

    return out


def part2(files, free_space):

    filled_space = [[] for _ in range(len(free_space))]
    space_dict = {n: [] for n in range(10)}
    for index, space in enumerate(free_space):
        space_dict[space].append(index)
    file_index = len(files) - 1
    while file_index > 0:
        size, file_num = files[file_index]
        for i in range(file_index):
            if free_space[i] >= size:
                free_space[i] -= size
                filled_space[i].append((size, file_num))
                files[file_index] = (size, 0)
                break
        file_index -= 1

    out = []
    for i in range(len(files)):
        out.append(files[i])
        for j in range(len(filled_space[i])):
            out.append(filled_space[i][j])
        out.append((free_space[i], 0))
    return out


def solve(input_data):
    files, free_space = parse(input_data)
    p1 = p2 = 0

    count = 0
    for amount, num in part1(files.copy(), free_space.copy()):
        for _ in range(amount):
            p1 += (count) * int(num)
            count += 1

    count = 0
    for amount, num in part2(files, free_space):
        for _ in range(amount):
            p2 += (count) * int(num)
            count += 1

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 9)

    ex1, ex2 = solve(puzzle.examples[0].input_data)
    p1, p2 = profile(solve, puzzle.input_data)

    assert ex1 == 1928
    puzzle.answer_a = p1
    assert ex2 == 2858
    puzzle.answer_b = p2
