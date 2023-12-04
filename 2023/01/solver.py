import re


with open("input") as f:
    text = f.read().strip()

part1 = re.sub("[a-z]", "", text).split("\n")

part2 = (
    text.replace("one", "o1e")
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


def get_sum(lines):
    return sum(int(line[0] + line[-1]) for line in lines)


print("Part 1:", get_sum(part1))
print("Part 2:", get_sum(part2))
