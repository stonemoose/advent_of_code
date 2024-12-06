from collections import defaultdict
from itertools import permutations
from aocd.models import Puzzle
import re
import math


def parse(input_data):
    parsed = defaultdict(dict)
    for line in input_data.strip().split("\n"):
        regex = r"(\D+) would (\D+) (\d+) happiness units by sitting next to (\D+)."
        name, gain, points, other_name = re.match(regex, line).groups()
        if gain == "gain":
            parsed[name][other_name] = int(points)
        else:
            parsed[name][other_name] = -int(points)
    return parsed


def solver(seating_wishes):
    best = -math.inf
    for seating in permutations(seating_wishes):
        happiness = 0
        for person, other_person in zip(seating, seating[1:] + (seating[0],)):
            happiness += seating_wishes[person][other_person]
            happiness += seating_wishes[other_person][person]
        best = max(best, happiness)

    return best


def solve(input_data):
    seating_wishes = parse(input_data)
    p1 = solver(seating_wishes)

    new_seating_wishes = seating_wishes.copy()
    for person in seating_wishes:
        new_seating_wishes["me"][person] = 0
        new_seating_wishes[person]["me"] = 0
    p2 = solver(new_seating_wishes)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2015, 13)

    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
