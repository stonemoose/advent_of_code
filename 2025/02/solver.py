from aocd.models import Puzzle


def parse(input_data):
    parsed = []
    for line in input_data.split(","):
        start, end = line.split("-")
        parsed.append((int(start), int(end)))
    return parsed


def solve(input_data):
    p1 = p2 = 0
    ranges = parse(input_data)

    for start, end in ranges:
        for id_num in range(start, end + 1):
            str_num = str(id_num)
            length = len(str_num)

            if str_num[: length // 2] == str_num[length // 2 :]:
                p1 += id_num

            for n in range(2, length + 1):
                if length % n:
                    continue
                if str_num[: length // n] * n == str_num:
                    p2 += id_num
                    break

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 2)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
