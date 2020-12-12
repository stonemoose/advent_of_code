directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
north = east = 0
ship_north = ship_east = 0
wp_north, wp_east = (1, 10)
current_dir = 0
direction_dict = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}
with open('input') as f:
    for line in f.read().strip().split('\n'):
        instruction = line[0]
        num = int(line[1:])
        if instruction == 'R':
            current_dir += num//90
            current_dir %= 4
            for i in range(num // 90):
                wp_east, wp_north = wp_north, -wp_east
        elif instruction == 'L':
            current_dir -= num//90
            current_dir %= 4
            for i in range(num // 90):
                wp_east, wp_north = -wp_north, wp_east
        elif instruction == 'F':
            east += num * directions[current_dir][0]
            north += num * directions[current_dir][1]
            ship_north += num * wp_north
            ship_east += num * wp_east
        else:
            east += num * directions[direction_dict[instruction]][0]
            north += num * directions[direction_dict[instruction]][1]
            wp_east += num * directions[direction_dict[instruction]][0]
            wp_north += num * directions[direction_dict[instruction]][1]

print(f'Part 1: {abs(north) + abs(east)}')
print(f'Part 1: {abs(ship_north) + abs(ship_east)}')
