
def fish_by_day(day, fish_timers):
    for _ in range(day):
        fish_timers = [fish_timers[(i+1) % 9] for i in range(9)]
        fish_timers[6] += fish_timers[8]
    return fish_timers


if __name__ == '__main__':
    with open('input') as f:
        fish_timers = [0]*9
        for num in f.read().strip().split(','):
            fish_timers[int(num)] += 1

    print(f'Part 1: {sum(fish_by_day(80, fish_timers))}')
    print(f'Part 2: {sum(fish_by_day(256, fish_timers))}')
