from aocd.models import Puzzle


def parse(input_data):
    left, right = zip(
        *[[int(n) for n in line.split()] for line in input_data.strip().split("\n")]
    )
    return sorted(left), sorted(right)


def part1(left, right):
    ans = 0
    for l, r in zip(left, right):
        ans += abs(l - r)
    return ans


def part2(left, right):
    ans = 0
    for l in left:
        for r in right:
            if l == r:
                ans += l
    return ans


if __name__ == "__main__":
    puzzle = Puzzle(2024, 1)

    left, right = parse(puzzle.input_data)

    for example in puzzle.examples:
        assert part1(*parse(example.input_data)) == 11
    puzzle.answer_a = part1(left, right)

    for example in puzzle.examples:
        assert part2(*parse(example.input_data)) == 31
    puzzle.answer_b = part2(left, right)
