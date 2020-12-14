from itertools import product, chain
with open('input') as f:
    in_file = f.read().strip().split('\n')

memory = {}
for line in in_file:
    first, second = line.split(' = ')
    if first == 'mask':
        mask = second
    else:
        string = ''
        for digit, m_digit in zip(f'{int(second):036b}', mask):
            if m_digit == 'X':
                string += digit
            else:
                string += m_digit
        memory[first] = int(string, 2)


ans = 0
for key in memory:
    ans += memory[key]
print('Part1: ', ans)


def possible_locations(mask, mem):
    chars = [['0', '1'] if c == 'X' else [c] for c in mask]
    mem_str = f'{mem:036b}'
    for i in range(len(mem_str)):
        if mem_str[i] == '1' and mask[i] == '0':
            chars[i] = ['1']
    all_masks = chars[0]
    for char in chars[1:]:
        all_masks = [list(chain(prod[0], prod[1])) for prod in product(all_masks, char)]
    all_masks = [int(''.join(mask), 2) for mask in all_masks]
    return all_masks


memory = {}
for line in in_file:
    first, second = line.split(' = ')
    if first == 'mask':
        mask = second
    else:
        mem = int(first[4:-1])
        for loc in possible_locations(mask, mem):
            memory[loc] = int(second)

ans = 0
for key in memory:
    ans += memory[key]
print('Part2: ', ans)
