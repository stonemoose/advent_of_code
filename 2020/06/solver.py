part1 = 0
part2 = 0
with open('input') as f:
    for group in f.read().strip().split('\n\n'):
        part1 += len(set(group.replace('\n', '')))
        part2 += len(set.intersection(*[set(line) for line in group.split('\n')]))

print(part1)
print(part2)
