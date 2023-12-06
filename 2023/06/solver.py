with open("input") as f:
    # with open("ex") as f:
    times, distances = [l.split()[1:] for l in f]


def ways(time, dist):
    for i in range(time):
        if i * (time - i) > dist:
            return time - i * 2 + 1


part1 = 1
for time, dist in zip(times, distances):
    part1 *= ways(int(time), int(dist))

print("Part 1: ", part1)

part2 = ways(int("".join(times)), int("".join(distances)))
print("Part 2: ", part2)
