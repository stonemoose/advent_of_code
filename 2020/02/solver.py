import re
from aocd.models import Puzzle


def valid_password(line):
    min_l, max_l, letter, password = re.split(r"-| |: ", line.strip())
    min_l, max_l = int(min_l), int(max_l)
    return min_l <= password.count(letter) <= max_l


def valid_password_part_two(line):
    first, second, letter, password = re.split(r"-| |: ", line.strip())
    first, second = int(first) - 1, int(second) - 1
    return (password[first] == letter) ^ (password[second] == letter)


def solve(input_data):
    p1 = sum([valid_password(line) for line in input_data.splitlines()])
    p2 = sum([valid_password_part_two(line) for line in input_data.splitlines()])
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 2)
    p1, p2 = solve(puzzle.input_data)
    print("Part 1:", p1)
    print("Part 2:", p2)
