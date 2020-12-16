with open('input') as f:
    start_time, buses = f.read().strip().split('\n')

buses = enumerate(buses.split(','))
buses = [(i % int(bus), int(bus)) for i, bus in buses if not bus == 'x']
start_time = int(start_time)
t_delta = t = buses[0][1]

for i, bus in buses[1:]:
    while bus - (t % bus) != i:
        t += t_delta
    t_delta *= bus

first = min(buses, key=lambda x: x[1] - start_time % x[1])[1]
print(f'Part 1: {first * (first - (start_time % first))}')
print(f'Part 2: {t}')
