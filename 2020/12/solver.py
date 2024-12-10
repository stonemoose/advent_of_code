from aocd.models import Puzzle


def solve(input_data):
    north = east = ship_north = ship_east = 0
    direction = [1, 0]
    wp_north, wp_east = (1, 10)
    direction_dict = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }
    for line in input_data.split("\n"):
        instruction = line[0]
        num = int(line[1:])
        if instruction == "R":
            for i in range(num // 90):
                wp_east, wp_north = wp_north, -wp_east
                direction[0], direction[1] = direction[1], -direction[0]
        elif instruction == "L":
            for i in range(num // 90):
                wp_east, wp_north = -wp_north, wp_east
                direction[0], direction[1] = -direction[1], direction[0]
        elif instruction == "F":
            east += num * direction[0]
            north += num * direction[1]
            ship_north += num * wp_north
            ship_east += num * wp_east
        else:
            east += num * direction_dict[instruction][0]
            north += num * direction_dict[instruction][1]
            wp_east += num * direction_dict[instruction][0]
            wp_north += num * direction_dict[instruction][1]

    p1 = abs(north) + abs(east)
    p2 = abs(ship_north) + abs(ship_east)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 12)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
