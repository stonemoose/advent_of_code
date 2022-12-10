from aocd.models import Puzzle

puzzle = Puzzle(2022, 10)

input = [line.split() for line in puzzle.input_data.strip().split("\n")]


def solve(input):
    ans = 0
    x = [1, 1]
    cycles = [20, 60, 100, 140, 180, 220]
    for line in input * 5:
        x.append(x[-1])
        if line[0] == "addx":
            x.append(x[-1] + int(line[1]))
    return x


x = solve(input)[1:]
for i in range(6):
    for y in range(40):
        if x[i * 40 + y] in {y - 1, y, y + 1}:
            print("█", end="")
        else:
            print(" ", end="")
    print()
part1 = [20 + 40 * i for i in range(6)]
puzzle.answer_a = sum(x[i - 1] * i for i in part1)
puzzle.answer_b = "EHPZPJGL"
