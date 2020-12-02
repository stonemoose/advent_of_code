import re


def valid_password(line):
    min_l, max_l, letter, password = re.split(r'-| |: ', line.strip())
    min_l, max_l = int(min_l), int(max_l)
    return min_l <= password.count(letter) <= max_l


def valid_password_part_two(line):
    first, second, letter, password = re.split(r'-| |: ', line.strip())
    first, second = int(first), int(second)
    return (password[first] == letter) ^ (password[second] == letter)


print(sum([valid_password(line) for line in open('input').readlines()]))
print(sum([valid_password_part_two(line) for line in open('input').readlines()]))
