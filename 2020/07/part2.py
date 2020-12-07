import re
from collections import defaultdict

bags = defaultdict(list)

with open('input') as f:
    rules = f.read().strip().replace('no other bags', '').splitlines()

regex = r'(\d)? ?(\w* \w*) bag'
for rule in rules:
    main_bag, *extra_bags = re.findall(regex, rule)
    bags[main_bag[1]] = extra_bags


def contains_number(bag_rules, main_bag):
    num = 0
    for other_bag in bag_rules[main_bag]:
        n, bag = other_bag
        num += int(n) * contains_number(bag_rules, bag)
        num += int(n)
    print(f'{main_bag} can contain {num or 1} other bags')
    return num


def can_contain(bag_rules, first_bag):
    seen = set()
    look_for = [first_bag]
    for bag in look_for:
        for other_bag in bag_rules[bag]:
            if other_bag not in seen:
                look_for.append(other_bag)
                seen.add(other_bag)
    return seen


# print(len(can_contain(bags, 'shiny gold')))
print(contains_number(bags, 'shiny gold'))
