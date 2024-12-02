def deliver_presents(route, present_map):
    i = j = len(present_map) // 2
    for char in route:
        if char == ">":
            j += 1
        elif char == "<":
            j -= 1
        if char == "v":
            i += 1
        elif char == "^":
            i -= 1
        present_map[i][j] = 1


with open("input") as f:
    size = 200
    present_map = [[0 for i in range(size)] for i in range(size)]
    present_map2 = [[0 for i in range(size)] for i in range(size)]
    present_map[size // 2][size // 2] = 1
    present_map2[size // 2][size // 2] = 1

    instructions = f.read()
    deliver_presents(instructions, present_map)
    print(f"part 1: {sum(sum(line) for line in present_map)}")

    santa_route = instructions[::2]
    robot_route = instructions[1::2]
    deliver_presents(santa_route, present_map2)
    deliver_presents(robot_route, present_map2)
    print(f"part 2: {sum(sum(line) for line in present_map2)}")
