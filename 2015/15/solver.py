from re import findall
from aocd.models import Puzzle
import functools


def parse(input_data):
    ingredients = {}
    for line in input_data.strip().split("\n"):
        name, properties = line.split(":")
        ingredients[name] = [int(n) for n in findall(r"-?\d+", properties)]
    return ingredients


def solver(ingredients, num_props=4, calorie_limit=0):
    values = []
    best_value = 0
    for amounts in get_sums_to_n(len(ingredients)):
        amount_ingredients = list(zip(amounts, ingredients.values()))
        value, cal_count = get_cookie_value(amount_ingredients, num_props)
        if calorie_limit and cal_count != calorie_limit:
            value = 0
        values.append((value, cal_count))
        best_value = max(best_value, value)
    return best_value


@functools.cache
def get_sums_to_n(amount, n=100):
    if amount == 1:
        return [[n]]
    all_possible = []
    for i in range(1, n):
        for rest in get_sums_to_n(amount - 1, n - i):
            all_possible.append([i] + rest)
    return all_possible


def get_cookie_value(amount_ingredients, num_props):
    total = 1
    for i in range(num_props):
        curr = 0
        for amount, ingredient in amount_ingredients:
            curr += amount * ingredient[i]
        total *= max(curr, 0)

    cal_count = 0
    for amount, ingredient in amount_ingredients:
        cal_count += amount * ingredient[-1]
    return total, cal_count


def solve(input_data):
    parsed = parse(input_data)
    p1 = solver(parsed)
    p2 = solver(parsed, calorie_limit=500)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2015, 15)

    example_data = puzzle.examples[0].input_data
    example_parsed = parse(example_data)
    parsed = parse(puzzle.input_data)

    assert solver(example_parsed) == 62842880
    puzzle.answer_a = solver(parsed)

    assert solver(example_parsed, calorie_limit=500) == 57600000
    puzzle.answer_b = solver(parsed, calorie_limit=500)
