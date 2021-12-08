with open('input') as f:
    lines = [line.strip().split(' | ') for line in f.readlines()]
    lines = [([set(p) for p in segment_patterns.split()],
              [set(n) for n in output.split()])
             for segment_patterns, output in lines]


part1 = 0
part2 = 0
for patterns, output in lines:
    numbers = [None] * 10
    for pattern in list(patterns):
        num = 0
        if len(pattern) == 2:
            num = 1
        elif len(pattern) == 4:
            num = 4
        elif len(pattern) == 3:
            num = 7
        elif len(pattern) == 7:
            num = 8
        if num:
            numbers[num] = pattern
            patterns.remove(pattern)
    for pattern in patterns:
        if len(pattern) == 6:
            if numbers[4].issubset(pattern):
                num = 9
            elif numbers[1].issubset(pattern):
                num = 0
            else:
                num = 6
        elif numbers[1].issubset(pattern):
            num = 3
        elif len(pattern.intersection(numbers[4])) == 3:
            num = 5
        else:
            num = 2
        numbers[num] = pattern

    part2 += int(''.join([str(numbers.index(num)) for num in output]))
    part1 += len([num for num in output if numbers.index(num) in (1, 4, 7, 8)])

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
