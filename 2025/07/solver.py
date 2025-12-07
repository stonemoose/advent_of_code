from aocd.models import Puzzle
from collections import defaultdict


def parse(input_data):
    lines = input_data.split()
    parsed = []
    for line in lines:
        parsed.append(line)
    return parsed


def analyse_manifold(manifold):
    beams = defaultdict(int)
    beams[len(manifold[0]) // 2] = 1
    splits = 0
    quantum_timelines = 1
    for line in manifold:
        next_beams = defaultdict(int)
        for beam in beams:
            if line[beam] == "^":
                quantum_timelines += beams[beam]
                splits += 1
                next_beams[beam - 1] += beams[beam]
                next_beams[beam + 1] += beams[beam]
            else:
                next_beams[beam] += beams[beam]
        beams = next_beams
        print(beams)
    return splits, quantum_timelines


def solve(input_data):
    parsed = parse(input_data)
    p1, p2 = analyse_manifold(parsed)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 7)
    p1, p2 = solve(puzzle.input_data)
    print(p1, p2)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
