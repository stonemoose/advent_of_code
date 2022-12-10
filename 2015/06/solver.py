
def toggle(start, end, lights, lights2):
    if int(start[0]) > int(end[0]) or int(start[1]) > int(end[1]):
        raise Exception(start, end)
    for x in range(int(start[0]), int(end[0])+1):
        for y in range(int(start[1]), int(end[1])+1):
            lights[x][y] ^= 1
            lights2[x][y] += 2

def turn_on(start, end, lights, lights2):
    if int(start[0]) > int(end[0]) or int(start[1]) > int(end[1]):
        raise Exception(start, end)
    for x in range(int(start[0]), int(end[0])+1):
        for y in range(int(start[1]), int(end[1])+1):
            lights[x][y] = 1
            lights2[x][y] += 1

def turn_off(start, end, lights, lights2):
    if int(start[0]) > int(end[0]) or int(start[1]) > int(end[1]):
        raise Exception(start, end)
    for x in range(int(start[0]), int(end[0])+1):
        for y in range(int(start[1]), int(end[1])+1):
            lights[x][y] = 0
            if lights2[x][y] > 0:
                lights2[x][y] -= 1


lights = [[0]*1000 for i in range(1000)]
lights2 = [[0]*1000 for i in range(1000)]


with open('2015/06/input') as f:
    instructions = [line.strip() for line in f.readlines()]


for inst in instructions:
    match inst.split():
        case ["toggle", start, "through", end]:
            toggle(start.split(','), end.split(','), lights, lights2)
        case ["turn", "on", start, "through", end]:
            turn_on(start.split(','), end.split(','), lights, lights2)
        case ["turn", "off", start, "through", end]:
            turn_off(start.split(','), end.split(','), lights, lights2)

print("part 1:", sum(sum(n) for n in lights))
print("part 2:", sum(sum(n) for n in lights2))