from aocd.models import Puzzle
from functools import cache


def parse(input_data):
    return [line.split() for line in input_data.strip().split("\n")]


@cache
def possible_arrangements(line, groups, current_group=0):
    if len(line) == 0:
        arr_len = len(groups)
        return arr_len == current_group == 0 or (
            arr_len == 1 and groups[0] == current_group
        )

    match line[0]:
        case ".":
            if groups and current_group == groups[0]:
                return possible_arrangements(line[1:], groups[1:])
            elif current_group == 0:
                return possible_arrangements(line[1:], groups)
            return 0

        case "#":
            if groups and current_group < groups[0]:
                return possible_arrangements(line[1:], groups, current_group + 1)
            return 0

        case "?":
            if groups and current_group == groups[0]:
                return possible_arrangements(line[1:], groups[1:])
            elif current_group == 0:
                operational = possible_arrangements(line[1:], groups)
                damaged = possible_arrangements(line[1:], groups, current_group + 1)
                return operational + damaged
            elif groups and current_group < groups[0]:
                return possible_arrangements(line[1:], groups, current_group + 1)
            return 0


def solve(rows, part=1):
    sum_possible = 0
    for springs, groups in rows:
        if part == 2:
            springs = "?".join([springs] * 5)
            groups = ",".join([groups] * 5)
        groups = tuple(int(n) for n in groups.split(","))
        sum_possible += possible_arrangements(springs, groups)

    return sum_possible


if __name__ == "__main__":
    puzzle = Puzzle(2023, 12)

    ex = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
    """
    parsed_ex = parse(ex)
    # for line in parsed_ex:
    #     print(line)
    assert solve(parsed_ex) == 21
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solve(parsed)
    assert solve(parsed_ex, 2) == 525152
    puzzle.answer_b = solve(parsed, 2)
