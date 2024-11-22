from re import findall
from aocd.models import Puzzle


def parse(input_data):
    aunts = {}
    for line in input_data.strip().split("\n"):
        name, info = line.split(":", 1)
        aunts[name] = {
            key: int(value) for key, value in findall("([a-z]+): (\d+)", info)
        }
    return aunts


def solve_1(aunts, correct_sue):
    for aunt, info in aunts.items():
        for key, value in correct_sue.items():
            if key in info and info[key] != value:
                break
        else:
            return aunt
    return "Did not find any match!!!!"


def solve_2(aunts, correct_sue):
    for aunt, info in aunts.items():
        for key, value in correct_sue.items():
            if key in info:
                if key in ["trees", "cats"]:
                    if info[key] <= value:
                        break
                elif key in ["pomeranians", "goldfish"]:
                    if info[key] >= value:
                        break
                else:
                    if info[key] != value:
                        break
        else:
            return aunt
    return "Did not find any match!!!!"


if __name__ == "__main__":
    puzzle = Puzzle(2015, 16)

    parsed = parse(puzzle.input_data)
    correct_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    print(solve_1(parsed, correct_sue))
    print(solve_2(parsed, correct_sue))
    puzzle.answer_a = int(solve_1(parsed, correct_sue).split()[-1])
    puzzle.answer_b = int(solve_2(parsed, correct_sue).split()[-1])
