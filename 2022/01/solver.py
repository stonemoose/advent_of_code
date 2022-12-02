with open("2022/01/input") as f:
    elves = f.read().strip().split("\n\n")

elves = sorted([sum(int(item) for item in elf.split("\n")) for elf in elves])

print("Part 1:", elves[-1])
print("Part 2:", sum(elves[-3:]))
