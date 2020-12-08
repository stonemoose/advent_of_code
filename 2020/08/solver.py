with open('input') as f:
    inputs = [line.split() for line in f.read().strip().split('\n')]


accumulator = 0
visited = list()
counter = 0

while True:
    op, num = inputs[counter]
    visited.append(counter)
    num = int(num)
    if op == 'acc':
        accumulator += num
        counter += 1
    if op == 'jmp':
        counter += num
    if op == 'nop':
        counter += 1
    if counter in visited:
        break
    if counter >= len(inputs):
        break

print(visited)
# look at visited list and manually change input for day 2 (line 299 jmp->nop)
print(counter)
print(accumulator)
