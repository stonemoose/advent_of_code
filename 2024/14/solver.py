import re
from aocd.models import Puzzle


def parse(input_data):
    out = []
    for line in input_data.split("\n"):
        nums = [int(n) for n in re.findall(r"[-+]?\d+", line)]
        pos = [nums[0], nums[1]]
        vel = (nums[2], nums[3])
        out.append((pos, vel))
    return out


def print_map(points, w, h):
    for y in range(h):
        for x in range(w):
            if (x, y) in points:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def safety_factor(robots, width, height):
    q1 = q2 = q3 = q4 = 0
    for point in robots:
        if point[0] < (width - 1) // 2:
            if point[1] < (height - 1) // 2:
                q1 += 1
            elif point[1] > (height - 1) // 2:
                q2 += 1
        elif point[0] > (width - 1) // 2:
            if point[1] < (height - 1) // 2:
                q3 += 1
            elif point[1] > (height - 1) // 2:
                q4 += 1
    return q1 * q2 * q3 * q4


def solve(input_data):
    parsed = parse(input_data)
    p1 = p2 = 0
    width = 101
    height = 103

    for point, velo in parsed:
        point[0] = (point[0] + velo[0] * 100) % width
        point[1] = (point[1] + velo[1] * 100) % height
    p1 = safety_factor((point for point, _ in parsed), width, height)

    for i in range(100, 101 * 103):
        for point, velo in parsed:
            point[0] = (point[0] + velo[0]) % width
            point[1] = (point[1] + velo[1]) % height
        robots = [tuple(p) for p, _ in parsed]
        # Assume all points are on seperate position for the picture
        if len(robots) == len(set(robots)):
            p2 = i + 1
            # print_map(robots, width, height)
            return p1, p2

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 14)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
