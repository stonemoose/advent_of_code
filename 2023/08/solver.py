import math


with open("input") as f:
    text = f.read().strip().split("\n")
    rules = [c == "R" for c in text[0]]
    dir_dict = {
        l.split("=")[0].strip(): l.split("=")[1].strip()[1:-1].split(", ")
        for l in text[2:]
    }


def find_end(current):
    steps = 0
    while current[-1] != "Z":
        current = dir_dict[current][rules[steps % len(rules)]]
        steps += 1
    return steps


print("Part 1:", find_end("AAA"))
all_starts = [path for path in dir_dict if path[-1] == "A"]
print("Part 2:", math.lcm(*(find_end(start) for start in all_starts)))
