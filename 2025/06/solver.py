from aocd.models import Puzzle
import math


def parse(input_data):
    *numbers, operators = input_data.split("\n")
    operators = operators.split()
    parsed_numbers = []
    for line in numbers:
        parsed_numbers.append([int(n) for n in line.split()])
    parsed_numbers = list(zip(*parsed_numbers))
    return list(zip(operators, parsed_numbers))


def cephalopod_parse(input_data):
    *numbers, operators = input_data.split("\n")
    operators = operators.split()
    numbers = list(zip(*numbers))
    parsed_numbers = [[]]
    for num in numbers:
        try:
            parsed_numbers[-1].append(int("".join(num)))
        except:
            parsed_numbers.append([])
    return list(zip(operators, parsed_numbers))


def solve_problem(operator, numbers):
    if operator == "*":
        return math.prod(numbers)
    return sum(numbers)


def solve(input_data):
    p1 = p2 = 0
    problems = parse(input_data)
    for operator, numbers in problems:
        p1 += solve_problem(operator, numbers)
    rotated_problems = cephalopod_parse(input_data)
    for operator, numbers in rotated_problems:
        p2 += solve_problem(operator, numbers)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 6)
    p1, p2 = solve(puzzle.input_data)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
