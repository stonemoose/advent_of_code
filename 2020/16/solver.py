import re

with open('input') as f:
    rules, my_ticket, nearby_tickets = f.read().strip().split('\n\n')


def make_rule(nums):
    a, b, x, y = [int(n) for n in nums]
    return lambda n: a <= n <= b or x <= n <= y


rules_dict = {}
for line in rules.split('\n'):
    name = line[:line.index(':')]
    for nums in re.findall(r'(\d*)-(\d*) or (\d*)-(\d*)', line):
        rules_dict[name] = make_rule(nums)

invalid = []
valid = []
for ticket in nearby_tickets.split('\n')[1:]:
    valid_ticket = True
    possible_list = []
    for num in ticket.split(','):
        possible = set(rule for rule in rules_dict if rules_dict[rule](int(num)))
        if possible:
            possible_list.append(possible)
        else:
            invalid.append(int(num))
            valid_ticket = False
    if valid_ticket:
        valid.append(possible_list)

print(f'Part 1: {sum(invalid)}')

possibles = []
for i in range(len(rules_dict)):
    possibles.append([i, set.intersection(*[ticket[i] for ticket in valid])])
taken = set()
correct_rules = {}
for poss in sorted(possibles, key=lambda x: x[1]):
    poss[1] -= taken
    if len(poss[1]) == 1:
        only_possible = poss[1].pop()
        taken.add(only_possible)
        correct_rules[only_possible] = poss[0]
    else:
        print(poss)

my_ticket = my_ticket.split('\n')[1]
my_ticket = [int(num) for num in my_ticket.split(',')]

ans = 1
for field in correct_rules:
    print(f'{field} = {my_ticket[correct_rules[field]]}')
    if re.match(r'departure*', field):
        ans *= my_ticket[correct_rules[field]]
print(ans)
