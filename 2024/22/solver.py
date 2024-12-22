from aocd.models import Puzzle
from collections import defaultdict
from functools import cache


def parse(input_data):
    return [int(n) for n in input_data.split("\n")]


@cache
def next_secret_number(number):
    number ^= number << 6
    number %= 16777216
    number ^= number >> 5
    number %= 16777216
    number ^= number << 11
    number %= 16777216
    return number


def get_sequence_values(price_diff):
    best_prices = {}
    for i in range(len(price_diff) - 3):
        diff = (
            price_diff[i][1],
            price_diff[i + 1][1],
            price_diff[i + 2][1],
            price_diff[i + 3][1],
        )
        price = price_diff[i + 3][0]
        if diff in best_prices:
            continue
        best_prices[diff] = price
    return best_prices


def solve(input_data):
    parsed = parse(input_data)
    p1 = p2 = 0
    sequence_bananas = defaultdict(int)
    for num in parsed:
        digit_change = [(int(str(num)[-1]), None)]
        for i in range(2000):
            num = next_secret_number(num)
            last_digit = int(str(num)[-1])
            digit_change.append((last_digit, last_digit - digit_change[i][0]))
        for sequence, value in get_sequence_values(digit_change[1:]).items():
            sequence_bananas[sequence] += value
        p1 += num
    p2 = max(sequence_bananas.values())
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 22)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
