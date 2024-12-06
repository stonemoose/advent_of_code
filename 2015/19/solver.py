import re
from aocd.models import Puzzle
from aoc_functionality import grid_helper as gh


def parse(input_data):
    rules = []
    replacements, start_molecule = input_data.strip().split("\n\n")
    for line in replacements.split("\n"):
        from_mol, to_mol = line.split(" => ")
        rules.append((from_mol, to_mol))
    return rules, start_molecule


def possible_replacements(molecule, rules):
    possible_molecules = set()
    for rule in rules:
        for match in re.finditer(rule[0], molecule):
            new_mol = molecule[: match.start(0)] + rule[1] + molecule[match.end(0) :]
            possible_molecules.add(new_mol)
    return possible_molecules


def reverse_find_medicine(rules, start_molecule):
    goal = "e"
    steps = 0
    rules = [(r[1], r[0]) for r in rules]
    print(start_molecule)
    print(rules)
    possible = {start_molecule}
    already_seen = set()
    while goal not in possible:
        steps += 1
        next_possible = set()
        for molecule in possible:
            next_possible |= possible_replacements(molecule, rules)
        next_possible -= already_seen
        already_seen |= next_possible
        possible = next_possible
        print(len(possible))
        length = 0
        for pos in possible:
            length += len(pos)
        print(f"average: {length/len(possible)}")
    return steps


def solve(input_data):
    p1 = p2 = 0
    rules, start_molecule = parse(input_data)
    possible = possible_replacements(start_molecule, rules)
    p1 = len(possible)

    # p2 = reverse_find_medicine(rules, start_molecule)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2015, 19)

    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1

    puzzle.answer_b = p2
