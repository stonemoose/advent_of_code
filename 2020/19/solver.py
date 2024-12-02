from functools import lru_cache
import re


with open("input") as f:
    rules, messages = [lines.split("\n") for lines in f.read().strip().split("\n\n")]
    rules = dict(rule.replace('"', "").split(": ") for rule in rules)


@lru_cache
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
print("Part 1: ", sum(bool(re.fullmatch(regex, m)) for m in messages))

make_regex.cache_clear()
rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"
regex = r"^" + make_regex("0") + r"$"
print("Part 2: ", sum(bool(re.fullmatch(regex, m)) for m in messages))
