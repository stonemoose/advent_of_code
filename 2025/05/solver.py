from aocd.models import Puzzle


def parse(input_data):
    parsed_ranges = []
    parsed_ids = []
    ranges, ids = input_data.split("\n\n")
    for line in ranges.split():
        start, end = line.split("-")
        parsed_ranges.append([int(start), int(end)])
    for line in ids.split():
        parsed_ids.append(int(line))
    return parsed_ranges, parsed_ids


def combine_ranges(ranges):
    combined = []
    for cur_range in ranges:
        start, end = cur_range
        for other_range in combined:
            other_start, other_end = other_range
            if start <= other_end and other_start <= end:
                other_range[0] = min(start, other_start)
                other_range[1] = max(end, other_end)
                break
        else:
            combined.append(cur_range)
    return combined


def solve(input_data):
    p1 = p2 = 0
    ranges, ids = parse(input_data)

    combined = combine_ranges(ranges)
    prev = []
    while combined != prev:
        prev = combined
        combined = combine_ranges(combined)

    for food_id in ids:
        for start, end in combined:
            if start <= food_id <= end:
                p1 += 1
                break
    for start, end in combined:
        p2 += end - start + 1

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 5)
    p1, p2 = solve(puzzle.input_data)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
