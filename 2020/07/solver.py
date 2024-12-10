import re
from collections import defaultdict
from aocd.models import Puzzle


def can_contain(bag_rules, first_bag):
    seen = set()
    look_for = [first_bag]
    for bag in look_for:
        for other_bag in bag_rules[bag]:
            if other_bag not in seen:
                look_for.append(other_bag)
                seen.add(other_bag)
    return seen


def contains_number(bag_rules, main_bag, debug=False):
    num = 0
    for other_bag in bag_rules[main_bag]:
        n, bag = other_bag
        num += int(n) * contains_number(bag_rules, bag)
        num += int(n)
    if debug:
        print(f"{main_bag} can contain {num or 1} other bags")
    return num


def part1_bags(rules):
    bags = defaultdict(set)
    regex = r"(?:\d )?(\w* \w*) bag"
    for rule in rules:
        main_bag, *extra_bags = re.findall(regex, rule)
        for bag in extra_bags:
            bags[bag].add(main_bag)
    return bags


def part2_bags(rules):
    bags = defaultdict(set)
    regex = r"(\d)? ?(\w* \w*) bag"
    for rule in rules:
        main_bag, *extra_bags = re.findall(regex, rule)
        bags[main_bag[1]] = extra_bags
    return bags


def solve(input_data):
    rules = input_data.replace("no other bags", "").splitlines()
    p1_bags = part1_bags(rules)
    p1 = len(can_contain(p1_bags, "shiny gold"))
    p2_bags = part2_bags(rules)
    p2 = contains_number(p2_bags, "shiny gold")
    return p1, p2


if __name__ == "__main__":

    puzzle = Puzzle(2020, 7)

    p1, p2 = solve(puzzle.input_data)
    print("Part 1:", p1)
    print("Part 2:", p2)
