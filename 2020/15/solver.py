with open('input') as f:
    numbers = {int(n): i for i, n in enumerate(f.read().strip().split(','))}

print(numbers)
prev = 0
for i in range(len(numbers), 29999999):
    spoken = i - numbers[prev] if prev in numbers else 0
    numbers[prev] = i
    prev = spoken
print(prev)
