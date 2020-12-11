from copy import deepcopy


def neighours(x, y, seats):
    num = -(seats[x][y] == '#')
    for i in range(max(0, x-1), x+2):
        for j in range(max(0, y-1), y+2):
            try:
                num += seats[i][j] == '#'
            except IndexError:
                continue
    return num


with open('input') as f:
    orig_seats = [[c for c in line] for line in f.read().strip().split('\n')]

seats = deepcopy(orig_seats)
old_seats = []
while old_seats != seats:
    old_seats = deepcopy(seats)
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if seats[row][col] == '.':
                continue
            n = neighours(row, col, old_seats)
            if n == 0:
                seats[row][col] = '#'
            elif n >= 4:
                seats[row][col] = 'L'
print(sum(x == '#' for line in seats for x in line))


def part2_neighours(x, y, seats):
    num = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            row = x+i
            col = y+j
            try:
                while row >= 0 <= col:
                    if seats[row][col] == '#':
                        num += 1
                        break
                    if seats[row][col] == 'L':
                        break
                    row += i
                    col += j
            except IndexError:
                continue
    return num


seats = deepcopy(orig_seats)
old_seats = []
while old_seats != seats:
    old_seats = deepcopy(seats)
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if seats[row][col] == '.':
                continue
            n = part2_neighours(row, col, old_seats)
            if n == 0:
                seats[row][col] = '#'
            elif n >= 5:
                seats[row][col] = 'L'

print(sum(x == '#' for line in seats for x in line))
