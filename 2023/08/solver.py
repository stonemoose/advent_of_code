import math


def find_end(current, dir_dict, rules):
    steps = 0
    while current[-1] != "Z":
        current = dir_dict[current][rules[steps % len(rules)]]
        steps += 1
    return steps


def solve(input_data):
    text = input_data.split("\n")
    rules = [c == "R" for c in text[0]]
    dir_dict = {
        l.split("=")[0].strip(): l.split("=")[1].strip()[1:-1].split(", ")
        for l in text[2:]
    }

    p1 = find_end("AAA", dir_dict, rules)
    all_starts = [path for path in dir_dict if path[-1] == "A"]
    p2 = math.lcm(*(find_end(start, dir_dict, rules) for start in all_starts))

    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        p1, p2 = solve(f.read().strip())

    print("Part 1:", p1)
    print("Part 2:", p2)
