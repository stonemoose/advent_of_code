import re


rules = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193
                  or x[-2:] == "in" and 59 <= int(x[:-2]) <= 76,
    'hcl': lambda x: re.fullmatch(r'#[0-9a-f]{6}', x),
    'ecl': lambda x: re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', x),
    'pid': lambda x: re.fullmatch(r'[0-9]{9}', x)
}

part1 = 0
part2 = 0

with open("input") as f:
    for passport in f.read().split("\n\n"):
        p_fields = dict(re.findall(r'(\w{3}):(\S+)\s?', passport))
        if set(rules).issubset(set(p_fields)):
            part1 += 1
            part2 += all(rules[field](p_fields[field]) for field in rules)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
