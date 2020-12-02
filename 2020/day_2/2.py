def valid_password(line):
    rule, password = line.strip().split(': ')
    min_l, max_l = rule.split('-')
    max_l, letter = max_l[:-2], max_l[-1]
    min_l = int(min_l)
    max_l = int(max_l)
    return min_l <= password.count(letter) <= max_l


print(sum([valid_password(line) for line in open('input').readlines()]))


def valid_password_part_two(line):
    rule, password = line.strip().split(': ')
    first, second = rule.split('-')
    second, letter = second[:-2], second[-1]
    first = int(first)-1
    second = int(second)-1
    return (password[first] == letter) ^ (password[second] == letter)


print(sum([valid_password_part_two(line) for line in open('input').readlines()]))
