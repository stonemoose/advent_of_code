from collections import Counter, defaultdict
from aocd.models import Puzzle


def parse(input_data):
    numbers = [0] + sorted([int(n) for n in input_data.split("\n")])
    numbers.append(numbers[-1] + 3)
    return numbers


def solve(input_data):
    numbers = parse(input_data)
    possible = defaultdict(int, {num: 0 for num in numbers})
    possible[numbers[-1]] = 1
    for i in range(len(numbers) - 1, 0, -1):
        possible[numbers[i] - 3] += possible[numbers[i]]
        possible[numbers[i] - 2] += possible[numbers[i]]
        possible[numbers[i] - 1] += possible[numbers[i]]
        numbers[i] = numbers[i] - numbers[i - 1]

    counts = Counter(numbers)
    p1 = counts[1] * (counts[3])
    p2 = possible[0]
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 10)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
