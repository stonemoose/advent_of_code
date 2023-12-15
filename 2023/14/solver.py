from aocd.models import Puzzle
import copy


def parse(input_data):
    return [list(line) for line in input_data.strip().split("\n")]


def find_first_open(line):
    for i in range(len(line) - 2, -1, -1):
        if line[i] in "#O":
            return i + 1
    return 0


def tilt_south(stones):
    new_stones = copy.deepcopy(stones)
    for y in range(len(stones) - 1, -1, -1):
        for x in range(len(stones[0])):
            if stones[y][x] == "O":
                open_y = find_first_open(
                    [new_stones[i][x] for i in range(y, len(stones))][::-1]
                )
                new_stones[y][x] = "."
                new_stones[len(stones) - 1 - open_y][x] = "O"

    return new_stones


def tilt_north(stones):
    new_stones = copy.deepcopy(stones)
    for y in range(len(stones)):
        for x in range(len(stones[0])):
            if stones[y][x] == "O":
                open_y = find_first_open([new_stones[i][x] for i in range(y + 1)])
                new_stones[y][x] = "."
                new_stones[open_y][x] = "O"
    return new_stones


def tilt_west(stones):
    new_stones = copy.deepcopy(stones)
    for x in range(len(stones[0])):
        for y in range(len(stones)):
            if stones[y][x] == "O":
                open_x = find_first_open(new_stones[y][: x + 1])
                new_stones[y][x] = "."
                new_stones[y][open_x] = "O"
    return new_stones


def tilt_east(stones):
    new_stones = copy.deepcopy(stones)
    for x in range(len(stones[0]) - 1, -1, -1):
        for y in range(len(stones)):
            if stones[y][x] == "O":
                open_x = find_first_open(new_stones[y][x:][::-1])
                new_stones[y][x] = "."
                new_stones[y][len(stones[0]) - 1 - open_x] = "O"
    return new_stones


def spin_cycle(stones, cycles):
    tilt_funcs = [tilt_north, tilt_west, tilt_south, tilt_east]
    last_maps = []

    for i in range(cycles):
        if stones in last_maps:
            index = last_maps.index(stones)
            repeats = i - index
            rest = (cycles - index) % repeats
            return last_maps[index + rest]
        last_maps.append(stones)
        for tilt_func in tilt_funcs:
            stones = tilt_func(stones)
    return stones


def solve(parsed, tilts=-1):
    ans = 0
    if tilts == -1:
        new_stones = tilt_north(parsed)
    else:
        new_stones = spin_cycle(parsed, tilts)
    for n, line in enumerate(new_stones):
        for stone in line:
            if stone == "O":
                ans += len(new_stones) - n

    return ans


if __name__ == "__main__":
    puzzle = Puzzle(2023, 14)

    parsed_ex = parse(puzzle.example_data)
    assert solve(parsed_ex) == 136
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solve(parsed)
    assert solve(parsed_ex, 1_000_000_000) == 64
    puzzle.answer_b = solve(parsed, 1_000_000_000)
