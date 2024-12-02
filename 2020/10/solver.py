from collections import Counter, defaultdict


with open("input") as f:
    numbers = [0] + sorted([int(n) for n in f.read().strip().split("\n")])
numbers.append(numbers[-1] + 3)

possible = defaultdict(int, {num: 0 for num in numbers})
possible[numbers[-1]] = 1
for i in range(len(numbers) - 1, 0, -1):
    possible[numbers[i] - 3] += possible[numbers[i]]
    possible[numbers[i] - 2] += possible[numbers[i]]
    possible[numbers[i] - 1] += possible[numbers[i]]
    numbers[i] = numbers[i] - numbers[i - 1]

counts = Counter(numbers)
print(f"{counts[1]*(counts[3])}")
print(f"{possible[0]}")
