def solve(input_data):
    part1 = part2 = 0
    for group in input_data.split("\n\n"):
        part1 += len(set(group.replace("\n", "")))
        part2 += len(set.intersection(*[set(line) for line in group.split("\n")]))
    return part1, part2


if __name__ == "__main__":
    part1 = 0
    part2 = 0
    with open("input") as f:
        part1, part2 = f.read().strip()

    print(part1)
    print(part2)
