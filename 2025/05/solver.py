from aocd.models import Puzzle


def parse(input_data):
    parsed_ranges = []
    ranges, ids = input_data.split("\n\n")
    for line in ranges.split():
        start, end = line.split("-")
        parsed_ranges.append([int(start), int(end)])
    return parsed_ranges, [int(i) for i in ids]


def combine_ranges(ranges):
    sorted_ranges = sorted(ranges)
    combined = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        prev_end = combined[-1][1]
        if start <= prev_end:
            combined[-1][1] = max(end, prev_end)
        else:
            combined.append([start, end])
    return combined


def solve(input_data):
    p1 = p2 = 0
    ranges, ids = parse(input_data)
    ranges = combine_ranges(ranges)

    for food_id in ids:
        for start, end in ranges:
            if start <= food_id <= end:
                p1 += 1
                break
    for start, end in ranges:
        p2 += end - start + 1

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 5)
    p1, p2 = solve(puzzle.input_data)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
