
def fish_by_day(day, timer_dict):
    for _ in range(day):
        next_timer_dict = {i: timer_dict[i+1] for i in range(8)}
        next_timer_dict[8] = timer_dict[0]
        next_timer_dict[6] += timer_dict[0]
        timer_dict = next_timer_dict
    return timer_dict


if __name__ == '__main__':
    with open('input') as f:
        timer_dict = {i: 0 for i in range(9)}
        for num in f.read().strip().split(','):
            timer_dict[int(num)] += 1

    print(f'Part 1: {sum(fish_by_day(80, timer_dict).values())}')
    print(f'Part 2: {sum(fish_by_day(256, timer_dict).values())}')
