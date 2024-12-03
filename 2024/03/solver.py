import re
from aocd.models import Puzzle


def parse(input_data, part2=False):
    out = []
    enabled = True
    for line in input_data.strip().split("\n"):
        if part2:
            line_data = []
            for i in range(len(line)):
                if enabled and (m := re.match(r"^mul\(\d+,\d+\)", line[i:])):
                    line_data.append(m.group(0))
                if not enabled and re.match(r"^do\(\)", line[i:]):
                    enabled = True
                if enabled and re.match(r"^don't\(\)", line[i:]):
                    enabled = False

            out.append(line_data)
        else:
            out.append(re.findall(r"mul\(\d+,\d+\)", line))
    return out

def helper(line):
    out = 0
    for thing in line:
        nums = re.findall(r"\d+", thing)
        assert len(nums) == 2
        out += int(nums[0])*int(nums[1])
    return out

def solve(parsed):
    ans = 0
    for line in parsed:
        ans += helper(line)
    return ans


if __name__=="__main__":
    puzzle = Puzzle(2024, 3)

    parsed = parse(puzzle.input_data)
    ex = puzzle.examples[0]
    assert solve(parse(ex.input_data)) == 161
    puzzle.answer_a = solve(parsed)

    ex2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    assert solve(parse(ex2, part2=True)) == 48
    parsed = parse(puzzle.input_data, part2=True)
    puzzle.answer_b = solve(parsed)

