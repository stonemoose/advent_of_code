import re
from collections import defaultdict

bags = defaultdict(set)

with open('input') as f:
    rules = f.read().strip().replace('no other bags', '').splitlines()

regex = r'(?:\d )?(\w* \w*) bag'
for rule in rules:
    main_bag, *extra_bags = re.findall(regex, rule)
    for bag in extra_bags:
        bags[bag].add(main_bag)


def can_contain(bag_rules, first_bag):
    seen = set()
    look_for = [first_bag]
    for bag in look_for:
        for other_bag in bag_rules[bag]:
            if other_bag not in seen:
                look_for.append(other_bag)
                seen.add(other_bag)
    return seen


print(len(can_contain(bags, 'shiny gold')))
