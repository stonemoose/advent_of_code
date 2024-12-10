import re


def make_rule(nums):
    a, b, x, y = [int(n) for n in nums]
    return lambda n: a <= n <= b or x <= n <= y


def solve(input_data):
    rules, my_ticket, nearby_tickets = input_data.split("\n\n")
    rules_dict = {}
    for line in rules.split("\n"):
        name = line[: line.index(":")]
        for nums in re.findall(r"(\d*)-(\d*) or (\d*)-(\d*)", line):
            rules_dict[name] = make_rule(nums)

    invalid = []
    valid = []
    for ticket in nearby_tickets.split("\n")[1:]:

        possible_list = []
        valid_ticket = True
        for num in ticket.split(","):
            possible = set(rule for rule in rules_dict if rules_dict[rule](int(num)))
            if possible:
                possible_list.append(possible)
            else:
                invalid.append(int(num))
                valid_ticket = False
        if valid_ticket:
            valid.append(possible_list)

    p1 = sum(invalid)

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
            pass

    my_ticket = my_ticket.split("\n")[1]
    my_ticket = [int(num) for num in my_ticket.split(",")]

    p2 = 1
    for field in correct_rules:
        if re.match(r"departure*", field):
            p2 *= my_ticket[correct_rules[field]]
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        rules, my_ticket, nearby_tickets = f.read().strip().split("\n\n")
