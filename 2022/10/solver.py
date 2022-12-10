from aocd.models import Puzzle

puzzle = Puzzle(2022, 10)
input = [line.split() for line in puzzle.input_data.strip().split("\n")]

cycles = [1]
for line in input * 2:
    cycles.append(cycles[-1])
    if line[0] == "addx":
        cycles.append(cycles[-1] + int(line[1]))

for row in range(6):
    for pos in range(40):
        if cycles[row * 40 + pos] in {pos - 1, pos, pos + 1}:
            print("█", end="")
        else:
            print(" ", end="")
    print()

puzzle.answer_a = sum(cycles[i - 1] * i for i in [20, 60, 100, 140, 180, 220])
puzzle.answer_b = "EHPZPJGL"
