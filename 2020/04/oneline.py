import re

# Part 1
print(sum([len(re.findall(r'(byr:)|(iyr:)|(eyr:)|(hgt:)|(hcl:)|(ecl:)|(pid:)', p)) == 7 for p in open('input').read().split('\n\n')]))

# Part 2
print(sum([len(re.findall(r'(byr:(19[2-9]\d|200[0-2]))|(iyr:20(1\d|20))|(eyr:20(2\d|30))|(hgt:(1([5-8]\d|9[0-3])cm)|((59|6\d|7[0-6])in))|(hcl:#[0-9a-f]{6})|(ecl:amb|blu|brn|gry|grn|hzl|oth)|(pid:\d{9})(\s|$)', p)) == 7 for p in open('input').read().split('\n\n')]))
