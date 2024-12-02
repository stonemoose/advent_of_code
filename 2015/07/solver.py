from aocd.models import Puzzle
from collections import defaultdict

puzzle = Puzzle(2015, 7)


def parse(input_data):
    return dict(l.split(" -> ")[::-1] for l in input_data.split("\n"))


def solve(input_data, ans_wire):
    wires = parse(input_data)
    wire_cache = {}

    def get_value(wire):
        if wire in wire_cache:
            return wire_cache[wire]
        if wire.isdigit():
            return int(wire)

        match wires[wire].split():
            case [a]:
                val = get_value(a)
            case a, "AND", b:
                val = get_value(a) & get_value(b)
            case a, "OR", b:
                val = get_value(a) | get_value(b)
            case a, "LSHIFT", b:
                val = get_value(a) << int(b)
            case a, "RSHIFT", b:
                val = get_value(a) >> int(b)
            case "NOT", a:
                val = get_value(a) ^ 0xFFFF

        wire_cache[wire] = val
        return val

    part1 = get_value(ans_wire)

    wire_cache = {}
    wire_cache["b"] = part1
    part2 = get_value(ans_wire)
    return part1, part2


puzzle.answer_a, puzzle.answer_b = solve(puzzle.input_data, "a")
