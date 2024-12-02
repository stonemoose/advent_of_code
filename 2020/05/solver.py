import re


def make_binary(line):
    return int(re.sub("B|R", "1", re.sub(r"F|L", "0", line)), base=2)


with open("input") as f:
    passes = [make_binary(line) for line in f.read().splitlines()]
passes.sort()

# Part 1
print(max(passes))
# Part 2
print(set(range(passes[0], passes[-1])).difference(passes).pop())

# Part 2 manual uncomment lines under
# Look for where the last digit changes
for i, p in enumerate(passes):
    print(f"{p:3}", end=" ")
    if i % 10 == 9:
        print()
