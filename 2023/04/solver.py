def solve(input_data):
    text = [line.split(":")[1] for line in input_data.split("\n")]

    part1 = 0
    part2 = [1 for _ in range(len(text))]
    for i, games in enumerate(text):
        winning, numbers = [set(x.strip().split()) for x in games.split("|")]
        if len(winning & numbers):
            part1 += 2 ** (len(winning & numbers) - 1)
            for n in range(1, len(winning & numbers) + 1):
                part2[i + n] += part2[i]

    part2 = sum(part2)
    return part1, part2


if __name__ == "__main__":
    with open("input") as f:
        part1, part2 = solve(f.read().strip())

    print("Part1: ", part1)
    print("Part2: ", sum(part2))
