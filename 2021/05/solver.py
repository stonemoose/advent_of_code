
def inclusive_range(start, end, length):
    if start == end:
        return [start] * length
    if start > end:
        return list(range(start, end-1, -1))
    return list(range(start, end+1))


def add_line(start, end, coordinates):
    length = abs(start[0] - end[0] or start[1] - end[1]) + 1
    for i, j in zip(inclusive_range(start[0], end[0], length),
                    inclusive_range(start[1], end[1], length)):
        coordinates[i][j] += 1


if __name__ == '__main__':

    with open('input') as f:
        lines = [line.strip().split(' -> ') for line in f.readlines()]
        line_segments = {(
            tuple(map(int, start.split(','))),
            tuple(map(int, end.split(',')))
        ) for start, end in lines}

        straight_lines = set(filter(
            lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1],
            line_segments))
        diagonal_lines = line_segments - straight_lines

    coordinates = [[0]*1000 for i in range(1000)]

    for start, end in straight_lines:
        add_line(start, end, coordinates)
    print('Part 1', sum([num >= 2 for line in coordinates for num in line]))

    for start, end in diagonal_lines:
        add_line(start, end, coordinates)
    print('Part 2', sum([num >= 2 for line in coordinates for num in line]))
