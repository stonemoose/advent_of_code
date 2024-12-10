from aocd.models import Puzzle


def parse(input_data):
    return [int(n) for n in input_data.split("\n")]


def sum_of_earlier(num, earlier):
    return set(earlier).intersection(set(num - n for n in earlier))


def solve(input_data):
    numbers = parse(input_data)

    invalid = 0
    for i, num in enumerate(numbers[25:]):
        if not sum_of_earlier(num, numbers[i : i + 25]):
            invalid = num
            break

    p2 = 0
    for i in range(len(numbers)):
        sum_nums = numbers[i]
        if sum_nums == invalid:
            break

        for j in range(i + 1, len(numbers)):
            sum_nums += numbers[j]
            if sum_nums > invalid:
                break
            elif sum_nums == invalid:
                p2 = max(numbers[i : j + 1]) + min(numbers[i : j + 1])
                break
    return invalid, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 9)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
