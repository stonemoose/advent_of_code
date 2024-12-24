from aocd.models import Puzzle
from collections import defaultdict
from functools import cache


def parse(input_data):
    initial = {}
    gates = {}
    first, second = input_data.split("\n\n")
    for line in first.split("\n"):
        name, num = line.split(": ")
        initial[name] = int(num)

    for line in second.split("\n"):
        thing, name = line.split(" -> ")
        first, op, second = thing.split(" ")
        gates[name] = (first, op, second)
    return initial, gates


def test_nums(gates, wires, num):
    zs = []
    xs = []
    ys = []
    others = []
    wires = wires.copy()
    for wire in wires:
        wires[wire] = 0
    wires[f"x{num:0d}"] = 1
    wires[f"y{num:0d}"] = 1

    @cache
    def cached_help(wire):
        if wire.startswith("x"):
            xs.append(wire)
        elif wire.startswith("y"):
            ys.append(wire)
        elif wire.startswith("z"):
            zs.append(wire)
        else:
            others.append(wire)
        if wire in wires:
            return wires[wire]
        assert wire in gates
        first, op, second = gates[wire]
        match op:
            case "AND":
                return cached_help(first) & cached_help(second)
            case "OR":
                return cached_help(first) | cached_help(second)
            case "XOR":
                return cached_help(first) ^ cached_help(second)
            case _:
                raise Exception(f"unhandled {_}")

    for wire in gates:
        try:
            cached_help(wire)
        except RecursionError:
            return 0, 0, -1

    x_tot = y_tot = z_tot = 0

    for i, wire in enumerate(sorted(xs)):
        if cached_help(wire):
            x_tot += 2**i
    for i, wire in enumerate(sorted(ys)):
        if cached_help(wire):
            y_tot += 2**i
    for i, wire in enumerate(sorted(zs)):
        if cached_help(wire):
            z_tot += 2**i
    if not x_tot + y_tot == z_tot:
        print(num)
        print(f"{x_tot:b}")
        print(f"{y_tot:b}")
        print(f"{z_tot:b}, {z_tot}")
        print()
    return x_tot + y_tot == z_tot


def bfs(gates, starts):
    children = defaultdict(set)
    last_z = None
    for z in starts:
        queue = [z]
        while queue:
            current = queue.pop(0)
            children[z].add(current)
            if current in gates:
                n1, op, n2 = gates[current]
                queue.append(n1)
                queue.append(n2)
        children[z].remove(z)
        print(z, last_z, children[last_z] - children[z])
        last_z = z


def solve(input_data):
    p1 = p2 = 0
    wires, gates = parse(input_data)

    zs = []
    xs = []
    ys = []
    others = []

    @cache
    def cached_help(wire):
        if wire.startswith("x"):
            xs.append(wire)
        elif wire.startswith("y"):
            ys.append(wire)
        elif wire.startswith("z"):
            zs.append(wire)
        else:
            others.append(wire)
        if wire in wires:
            return wires[wire]
        assert wire in gates
        first, op, second = gates[wire]
        match op:
            case "AND":
                return cached_help(first) & cached_help(second)
            case "OR":
                return cached_help(first) | cached_help(second)
            case "XOR":
                return cached_help(first) ^ cached_help(second)
            case _:
                raise Exception(f"unhandled {_}")

    for wire in gates:
        cached_help(wire)

    for i, wire in enumerate(sorted(zs)):
        if cached_help(wire):
            p1 += 2**i

    problems = []
    # manual looking at wires that had problems using bfs and test_nums reveals:
    swaps = [("fph", "z15"), ("gds", "z21"), ("wrk", "jrs"), ("z34", "cqk")]
    p2 = []
    for s1, s2 in swaps:
        gates[s1], gates[s2] = gates[s2], gates[s1]
        p2.append(s1)
        p2.append(s2)
    bfs(gates, sorted(zs))
    for i in range(len(xs)):
        if not test_nums(gates, wires, i):
            problems.append(f"z{i:0d}")
    print(problems)
    p2 = ",".join(sorted(p2))
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 24)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
