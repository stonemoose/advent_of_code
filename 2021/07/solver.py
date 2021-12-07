from collections import Counter


def optimal_fuel_usage(fuel_function, positions):
    last_count = 1000000000
    for i in range(1000):
        count = 0
        for position, num in positions.items():
            count += fuel_function(abs(position - i)) * num
        if count > last_count:
            return last_count
        last_count, count = count, last_count


if __name__ == '__main__':
    with open('input') as f:
        positions = Counter([int(n) for n in f.readline().strip().split(',')])

    print(f'Part 1: {optimal_fuel_usage(lambda x: x, positions)}')
    print(f'Part 1: {optimal_fuel_usage(lambda x: x*(x+1)//2, positions)}')
