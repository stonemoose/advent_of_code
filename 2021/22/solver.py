cubes = set()

with open("input") as f:
    for line_num, line in enumerate(f):
        command, coords = line.strip().split()
        x, y, z = ([int(i) for i in c[2:].split("..")] for c in coords.split(","))
        print(command, x, y, z)
        for x_coord in range(x[0], x[1] + 1):
            for y_coord in range(y[0], y[1] + 1):
                for z_coord in range(z[0], z[1] + 1):
                    if command == "on":
                        cubes.add((x_coord, y_coord, z_coord))
                    else:
                        cubes.discard((x_coord, y_coord, z_coord))
        print(line_num)
        if line_num == 19:
            break

print(len(cubes))
