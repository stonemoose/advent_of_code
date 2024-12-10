import re


def solve(input_data):

    rules, messages = [lines.split("\n") for lines in input_data.split("\n\n")]
    rules = dict(rule.replace('"', "").split(": ") for rule in rules)

    def make_regex(rule_num, level=0):
        if level >= 20:
            return "x"
        rule = rules[rule_num].strip()
        if rule in "ab":
            return rule
        choices = rule.split("| ")
        reg = []
        for choice in choices:
            reg.append("".join(make_regex(rule, level + 1) for rule in choice.split()))
        return rf'({"|".join(reg)})'

    regex = r"^" + make_regex("0") + r"$"
    p1 = sum(bool(re.fullmatch(regex, m)) for m in messages)

    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"
    regex = r"^" + make_regex("0") + r"$"
    p2 = sum(bool(re.fullmatch(regex, m)) for m in messages)
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        p1, p2 = solve(f.read().strip())
    print("Part 1:", p1)
    print("Part 2:", p2)
