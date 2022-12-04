with open("input") as f:
    input_pairs = [line.split(",") for line in f.read().strip().split("\n")]


def make_section_range(sections):
    first, second = map(int, sections.split("-"))
    return set(range(first, second + 1))


part1 = part2 = 0
for first, second in input_pairs:
    first_range = make_section_range(first)
    second_range = make_section_range(second)
    if first_range <= second_range or first_range >= second_range:
        part1 += 1
    if first_range & second_range:
        part2 += 1


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
