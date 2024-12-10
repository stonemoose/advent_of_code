from itertools import product, chain
from aocd.models import Puzzle


def possible_locations(mask, mem):
    chars = [["0", "1"] if c == "X" else [c] for c in mask]
    mem_str = f"{mem:036b}"
    for i in range(len(mem_str)):
        if mem_str[i] == "1" and mask[i] == "0":
            chars[i] = ["1"]
    all_masks = chars[0]
    for char in chars[1:]:
        all_masks = [list(chain(prod[0], prod[1])) for prod in product(all_masks, char)]
    all_masks = [int("".join(mask), 2) for mask in all_masks]
    return all_masks


def parse(input_data):
    return [line.split(" = ") for line in input_data.split("\n")]


def solve(input_data):
    docking_data = parse(input_data)
    memory1 = {}
    memory2 = {}

    for first, second in docking_data:
        if first == "mask":
            mask = second
        else:
            string = ""
            for digit, m_digit in zip(f"{int(second):036b}", mask):
                if m_digit == "X":
                    string += digit
                else:
                    string += m_digit
            memory1[first] = int(string, 2)

            mem = int(first[4:-1])
            for loc in possible_locations(mask, mem):
                memory2[loc] = int(second)

    p1 = sum(memory1.values())
    p2 = sum(memory2.values())
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 14)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
