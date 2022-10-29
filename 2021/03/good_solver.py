with open('input') as f:
    bit_nums = sorted([line.strip() for line in f.readlines()])

part1 = ''
start = 0
end = len(bit_nums)
for index in range(len(bit_nums[0])):
    for i, line in enumerate(bit_nums[start:end], 1):
        if line[index] == '1':
            if i < (end - start)/2.0:
                start += i
                part1 += '1'
            else:
                end -= i
                part1 += '0'
            break

gamma = int(''.join(map(str, part1)), 2)
epsilon = (1 << len(bit_nums[0])) - 1 - gamma
print(f'{gamma:b}')
print(f'{epsilon:b}')
print(gamma*epsilon)
