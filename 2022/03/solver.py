with open("2022/03/input") as f:
    input = f.read().strip().split("\n")

value = {chr(ord("a") + i): i + 1 for i in range(26)}
value.update({chr(ord("A") + i): i + 27 for i in range(26)})

part1 = 0
for sack in input:
    middle = int(len(sack) / 2)
    for char in set(sack[:middle]) & set(sack[middle:]):
        part1 += value[char]


part2 = 0
for first, second, third in zip(input[::3], input[1::3], input[2::3]):
    for char in set(first) & set(second) & set(third):
        part2 += value[char]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
