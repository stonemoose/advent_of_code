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


def solve(instructions):
    size = 200
    present_map = [[0 for i in range(size)] for i in range(size)]
    present_map2 = [[0 for i in range(size)] for i in range(size)]
    present_map[size // 2][size // 2] = 1
    present_map2[size // 2][size // 2] = 1

    deliver_presents(instructions, present_map)
    p1 = sum(sum(line) for line in present_map)

    santa_route = instructions[::2]
    robot_route = instructions[1::2]
    deliver_presents(santa_route, present_map2)
    deliver_presents(robot_route, present_map2)
    p2 = sum(sum(line) for line in present_map2)

    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        p1, p2 = solve(f.read())

    print("Part 1:", p1)
    print("Part 2:", p2)
