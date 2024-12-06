import re


def get_sum(lines):
    return sum(int(line[0] + line[-1]) for line in lines)


def solve(input_data):
    part1 = re.sub("[a-z]", "", input_data).split("\n")

    part2 = (
        input_data.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )
    part2 = re.sub("[a-z]", "", part2).split("\n")

    p1 = get_sum(part1)
    p2 = get_sum(part2)
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        p1, p2 = solve(f.read().strip())

    print("Part 1:", p1)
    print("Part 2:", p2)
