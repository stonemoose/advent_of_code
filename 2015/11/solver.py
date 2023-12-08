import re
import string

from aocd.models import Puzzle

puzzle = Puzzle(2015, 11)


def parse(input_data):
    return input_data.strip()


letters = string.ascii_lowercase


def good_password(pw):
    two_pairs = len(re.findall(r"(.)\1", pw)) >= 2
    not_iol = len(re.findall(r"[iol]", pw)) == 0

    if not (not_iol and two_pairs):
        return False

    for i in range(len(pw) - 2):
        if pw[i : i + 3] in letters:
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


def solve(password):
    password = next_password(password)
    while not good_password(password):
        password = next_password(password)

    return password


puzzle.answer_a = solve(parse(puzzle.input_data))
puzzle.answer_b = solve(puzzle.answer_a)
