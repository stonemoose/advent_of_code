from aocd.models import Puzzle


def parse(input_data):
    return input_data.strip().split(",")


def get_hash(line):
    val = 0
    for char in line:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def solve(input_data):
    parsed = parse(input_data)
    boxes = {i: [] for i in range(256)}
    focal_lengths = {}
    sum_hashes = 0
    for line in parsed:
        match list(line):
            case *lbl, "=", num:
                label = "".join(lbl)
                hash = get_hash((label))
                focal_lengths[label] = int(num)
                if label not in boxes[hash]:
                    boxes[hash].append(label)

            case *lbl, "-":
                label = "".join(lbl)
                hash = get_hash((label))
                if label in boxes[hash]:
                    boxes[hash].remove(label)
        sum_hashes += get_hash(line)

    focusing_power = 0
    for i, box in enumerate(boxes, 1):
        for slot, lens in enumerate(boxes[box], 1):
            focusing_power += focal_lengths[lens] * slot * i

    return sum_hashes, focusing_power


if __name__ == "__main__":
    puzzle = Puzzle(2023, 15)

    assert solve(puzzle.examples[0].input_data) == (1320, 145)

    puzzle.answer_a, puzzle.answer_b = solve(puzzle.input_data)
