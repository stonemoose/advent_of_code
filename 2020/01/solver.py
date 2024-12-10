from aocd.models import Puzzle


def solve(input_data):
    num_list = [int(n) for n in input_data.splitlines()]
    for i in range(0, len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == 2020:
                p1 = num_list[i] * num_list[j]
            # b
            for k in range(j + 1, len(num_list)):
                if num_list[i] + num_list[j] + num_list[k] == 2020:
                    p2 = num_list[i] * num_list[j] * num_list[k]
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 1)
    p1, p2 = solve(puzzle.input_data)
    print("Part 1:", p1)
    print("Part 2:", p2)
