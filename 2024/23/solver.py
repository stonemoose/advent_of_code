from aocd.models import Puzzle
from collections import defaultdict


def parse(input_data):
    computer_connections = defaultdict(set)
    for line in input_data.split("\n"):
        comp1, comp2 = line.split("-")
        computer_connections[comp1].add(comp2)
        computer_connections[comp2].add(comp1)
    return computer_connections


seen = set()


def helper(lan_network, reachable, computers):
    global seen
    if frozenset(lan_network) in seen:
        return set()
    seen.add(frozenset(lan_network))

    if len(reachable) == 0:
        return lan_network

    biggest = lan_network
    for other_computer in sorted(reachable):
        if other_computer not in lan_network:
            other_reach = computers[other_computer] & reachable
            other_lan = helper(lan_network | {other_computer}, other_reach, computers)

            if len(other_lan) > len(biggest):
                biggest = other_lan
    return biggest


def solve(input_data):
    computers = parse(input_data)
    three_computers = set()
    for comp1 in computers:
        for comp2 in computers[comp1]:
            for other in computers[comp1] & computers[comp2]:
                three_computers.add(frozenset([comp1, comp2, other]))

    p1 = 0
    for group in three_computers:
        for comp in group:
            if comp.startswith("t"):
                p1 += 1
                break

    biggest_lan = helper(set(), set(computers), computers)
    p2 = ",".join(sorted(biggest_lan))

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 23)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
