north = east = ship_north = ship_east = 0
direction = [1, 0]
wp_north, wp_east = (1, 10)
direction_dict = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}
with open('input') as f:
    for line in f.read().strip().split('\n'):
        instruction = line[0]
        num = int(line[1:])
        if instruction == 'R':
            for i in range(num // 90):
                wp_east, wp_north = wp_north, -wp_east
                direction[0], direction[1] = direction[1], -direction[0]
        elif instruction == 'L':
            for i in range(num // 90):
                wp_east, wp_north = -wp_north, wp_east
                direction[0], direction[1] = -direction[1], direction[0]
        elif instruction == 'F':
            east += num * direction[0]
            north += num * direction[1]
            ship_north += num * wp_north
            ship_east += num * wp_east
        else:
            east += num * direction_dict[instruction][0]
            north += num * direction_dict[instruction][1]
            wp_east += num * direction_dict[instruction][0]
            wp_north += num * direction_dict[instruction][1]

print(f'Part 1: {abs(north) + abs(east)}')
print(f'Part 1: {abs(ship_north) + abs(ship_east)}')
