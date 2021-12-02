
lines = [line.strip().split(' ') for line in open('input').readlines()]

down = 0
forward = 0
aim = 0
for command, number in lines:
    number = int(number)
    if command == 'forward':
        forward += number
        down += aim * number
    elif command == 'down':
        aim += number
    elif command == 'up':
        aim -= number

print(f'Part 1: {aim*forward}')
print(f'Part 2: {down*forward}')
