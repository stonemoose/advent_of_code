def ways(time, dist):
    for i in range(time):
        if i * (time - i) > dist:
            return time - i * 2 + 1


def solve(input_data):
    times, distances = [l.split()[1:] for l in input_data.split("\n")]
    p1 = 1
    for time, dist in zip(times, distances):
        p1 *= ways(int(time), int(dist))

    p2 = ways(int("".join(times)), int("".join(distances)))
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        part1, part2 = solve(f.read())

    print("Part 1: ", part1)
    print("Part 2: ", part2)
