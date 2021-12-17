# target area: x=94..151, y=-156..-103

print(f'Part 1: {155*156//2}')

x_min = 94
x_max = 151
y_min = -156
y_max = -103

y_min_vel = -156
y_max_vel = 155
x_min_vel = 14
x_max_vel = 151

ans = 0
for y in range(y_min_vel, y_max_vel+1):
    for x in range(x_min_vel, x_max_vel+1):
        pos_x, pos_y = 0, 0
        vel_x, vel_y = x, y
        while pos_x <= x_max and pos_y >= y_min:
            pos_x += vel_x
            pos_y += vel_y
            if vel_x > 0:
                vel_x -= 1
            vel_y -= 1
            if x_min <= pos_x <= x_max and y_min <= pos_y <= y_max:
                ans += 1
                break


print(f'Part 2: {ans}')
