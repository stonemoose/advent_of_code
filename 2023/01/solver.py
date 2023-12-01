import re


with open("input") as f:
    data = f.read().strip()

part1 = re.sub("[a-z]", "", data).split("\n")

part2 = (
    data.replace("one", "o1e")
    .replace("two", "t2o")
    .replace("three", "t3e")
    .replace("four", "4")
    .replace("five", "5e")
    .replace("six", "6")
    .replace("seven", "7n")
    .replace("eight", "e8t")
    .replace("nine", "n9e")
)
part2 = re.sub("[a-z]", "", part2).split("\n")


def get_sum(lines):
    return sum(int(line[0] + line[-1]) for line in lines)


print("Part 1:", get_sum(part1))
print("Part 2:", get_sum(part2))
