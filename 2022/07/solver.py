with open("input") as f:
    input = f.read().strip().split("\n")


system = {"/": 0}
current_dir = ["/"]
counted = set()
for line in input[1:]:
    line = line.strip()
    if line[2:4] == "cd":
        if line[5:7] == "..":
            current_dir.pop()
        else:
            current_dir.append(line[5:])
            system["/".join(current_dir)] = 0
    elif line[2:4] == "ls":
        pass
    elif line.split()[0] == "dir":
        pass
    else:
        num, name = line.split()
        if not ("/".join(current_dir) + name) in counted:
            m = "/"
            system[m] += int(num)
            for x in current_dir[1:]:
                m += "/" + x
                system[m] += int(num)

            counted.add("/".join(current_dir) + name)

part1 = 0
for key, value in system.items():
    if value <= 100000:
        part1 += value
print(f"Part 1: {part1}")

free_space = 70000000 - system["/"]
possible = []
for key, value in system.items():
    if free_space + value >= 30000000:
        possible.append(value)
print(f"Part 2: {min(possible)}")
