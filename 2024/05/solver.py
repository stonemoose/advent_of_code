import re
from aocd.models import Puzzle


def parse(input_data):
    rules = {}
    pages = []
    lines, rest = input_data.strip().split("\n\n")
    for line in lines.split("\n"):
        nums = line.split("|")
        if int(nums[0]) in rules:
            rules[int(nums[0])].add(int(nums[1]))
        else:
            rules[int(nums[0])] = set()
            rules[int(nums[0])].add(int(nums[1]))
    for line in rest.split("\n"):
        nums = re.findall(r"\d+", line)
        pages.append([int(n) for n in nums])
    return rules, pages


def helper(line, rules):
    seen = set()
    print(rules)
    for thing in line:
        print(thing)
        print(seen)
        if thing in rules and rules[thing] & seen:
            return 0
        seen.add(thing)
    return line[len(line) // 2]


def helper2(line, rules):
    seen = set()
    for i, thing in enumerate(line):
        if thing in rules and rules[thing] & seen:
            line.pop(i)
            line.insert(i - 1, thing)
            return helper2(line, rules)
        seen.add(thing)
    return line[len(line) // 2]


def solve(input_data):
    rules, pages = parse(input_data)
    p1 = p2 = 0
    for line in pages:
        p1 += helper(line, rules)
        if not helper(line, rules):
            p2 += helper2(line, rules)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 5)
    p1, p2 = solve(puzzle.examples[0].input_data)
    print(p1)
    assert p1 == 143
    assert p2 == 123
    p1, p2 = solve(puzzle.input_data)
    print(p1, p2)
    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
