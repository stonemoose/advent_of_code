def flash(x, y, octopi):
    for i in range(max(0, x-1), x+2):
        for j in range(max(0, y-1), y+2):
            try:
                octopi[i][j] += 1
                if octopi[i][j] == 10:
                    flash(i, j, octopi)
            except IndexError:
                continue


with open('input') as f:
    octopi = [[int(n) for n in line.strip()] for line in f.readlines()]

flashes = 0
for step in range(1, 10000):
    for x in range(len(octopi)):
        for y in range(len(octopi[0])):
            octopi[x][y] += 1
            if octopi[x][y] == 10:
                flash(x, y, octopi)

    for x in range(len(octopi)):
        for y in range(len(octopi[0])):
            if octopi[x][y] >= 10:
                octopi[x][y] = 0
                flashes += 1

    if step == 100:
        print(f'Part 1: {flashes}')
    if not any(any(line) for line in octopi):
        print(f'Part 2: {step}')
        break
