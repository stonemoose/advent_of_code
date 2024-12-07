import re
from collections import defaultdict
from aocd.models import Puzzle


class Page(int):
    rulebook = defaultdict(set)

    def __new__(cls, num):
        return super().__new__(cls, num)

    def __lt__(self, other):
        return other in self.rulebook[self]


def parse(input_data):
    Page.rulebook = defaultdict(set)
    rules, updates = input_data.strip().split("\n\n")
    for line in rules.split("\n"):
        nums = line.split("|")
        Page.rulebook[Page(nums[0])].add(Page(nums[1]))

    return [[Page(page) for page in update.split(",")] for update in updates.split()]


def solve(input_data):
    updates = parse(input_data)
    p1 = p2 = 0
    for update in updates:
        sorted_update = sorted(update)
        if sorted_update == update:
            p1 += sorted_update[len(sorted_update) // 2]
        else:
            p2 += sorted_update[len(sorted_update) // 2]
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 5)
    for example in puzzle.examples:
        ex1, ex2 = solve(example.input_data)
        assert ex1 == int(example.answer_a)
        assert ex2 == int(example.answer_b)
    p1, p2 = solve(puzzle.input_data)
    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
