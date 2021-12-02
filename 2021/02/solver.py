
lines = [line.strip() for line in open('input').readlines()]

down = 0
forward = 0
aim = 0
for line in lines:
    command, number = line.split(' ')
    if command == 'forward':
        forward += int(number)
        down += aim * int(number)
    elif command == 'down':
        aim += int(number)
    elif command == 'up':
        aim -= int(number)

print('Part 1: ', aim*forward)
print('Part 2: ', down*forward)
