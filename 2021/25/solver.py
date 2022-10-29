from copy import deepcopy


with open('input') as f:
    square = ([[n for n in line.strip()] for line in f.readlines()])

size_i = len(square)
size_j = len(square[0])

step = 0
while True:
    step += 1
    new_square = deepcopy(square)
    for i in range(size_i):
        for j in range(size_j):
            if square[i][j] == '>' and square[i][(j+1) % size_j] == '.':
                new_square[i][j] = '.'
                new_square[i][(j+1) % size_j] = '>'
    mid_square = deepcopy(new_square)
    for i in range(size_i):
        for j in range(size_j):
            if mid_square[i][j] == 'v' and mid_square[(i+1) % size_i][j] == '.':
                new_square[i][j] = '.'
                new_square[(i+1) % size_i][j] = 'v'
    if square == new_square:
        break
    else:
        square = new_square

print(step)
