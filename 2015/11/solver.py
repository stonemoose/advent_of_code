import re
import string

from aocd.models import Puzzle


def parse(input_data):
    return input_data.strip()


def good_password(pw):
    two_pairs = len(re.findall(r"(.)\1", pw)) >= 2
    not_iol = len(re.findall(r"[iol]", pw)) == 0

    if not (not_iol and two_pairs):
        return False

    for i in range(len(pw) - 2):
        if pw[i : i + 3] in string.ascii_lowercase:
            return True
    return False


def next_password(pw):
    new_pw = []
    increased = False
    for i, letter in enumerate(pw[::-1], 1):
        if increased:
            new_pw.insert(0, letter)
        elif letter == "z":
            new_pw.insert(0, "a")
        else:
            new_pw.insert(0, chr(ord(letter) + 1))
            increased = True
    return "".join(new_pw)


def solver(password):
    password = next_password(password)
    while not good_password(password):
        password = next_password(password)

    return password


def solve(input_data):
    p1 = solver(parse(input_data))
    p2 = solver(p1)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2015, 11)
    puzzle.answer_a = solver(parse(puzzle.input_data))
    puzzle.answer_b = solver(puzzle.answer_a)
