from aocd.models import Puzzle


def parse(input_data):
    out = []
    for line in input_data.strip().split("\n"):
        out.append(line)
    return out


def helper(line, word="XMAS"):
    ret = 0
    for i in range(len(line)):
        if line[i:].startswith(word):
            ret += 1
        elif line[i:].startswith(word[::-1]):
            ret += 1
    print(line, ret)
    return ret


def helper2(square):
    diag1 = "".join(square[i][i] for i in range(3))
    diag2 = "".join(square[i][-1 - i] for i in range(3))
    if diag1 in ("MAS", "SAM") and diag2 in ("MAS", "SAM"):
        return 1
    return 0


def solve(parsed):
    p1 = p2 = 0
    for line in parsed:
        p1 += helper(line)
        pass
    for i in range(len(parsed[0])):
        pass
        p1 += helper("".join([l[i] for l in parsed]))
        p1 += helper(
            "".join([l[i + j] for j, l in enumerate(parsed) if i + j < len(l)])
        )
        p1 += helper("".join([l[i - j] for j, l in enumerate(parsed) if i - j >= 0]))
    for i, line in enumerate(parsed[1:], 1):
        pass
        p1 += helper("".join([l[j] for j, l in enumerate(parsed[i:])]))
        p1 += helper("".join([l[-j] for j, l in enumerate(parsed[i:], 1)]))

    for i in range(len(parsed) - 2):
        for j in range(len(parsed[0]) - 2):
            square = [line[j : j + 3] for line in parsed[i : i + 3]]
            p2 += helper2(square)

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 4)

    parsed = parse(puzzle.input_data)

    p1, p2 = solve(parsed)
    ex = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
    assert solve(parse(ex))[0] == 18
    if p1:
        puzzle.answer_a = p1
    assert solve(parse(ex))[1] == 9
    if p2:
        puzzle.answer_b = p2
