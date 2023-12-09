from re import findall
from aocd.models import Puzzle


def parse(input_data):
    return [
        [int(n) for n in findall("\d+", line)]
        for line in input_data.strip().split("\n")
    ]


def get_distances(parsed, race_time=1000):
    all_distances = []

    for line in parsed:
        distance = time = 0
        speed, speed_time, rest_time = line

        while time + speed_time <= race_time:
            distance += speed_time * speed
            time += speed_time + rest_time
        remaining_time = race_time - time
        if remaining_time > 0:
            distance += remaining_time * speed

        all_distances.append(distance)

    return all_distances


def get_most_points(parsed, race_time=1000):
    points = [0] * len(parsed)
    for seconds in range(1, race_time + 1):
        all_distances = get_distances(parsed, seconds)
        for i, dist in enumerate(all_distances):
            if dist == max(all_distances):
                points[i] += 1
    return max(points)


if __name__ == "__main__":
    puzzle = Puzzle(2015, 14)

    example_data = """
    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
    """
    example_parsed = parse(example_data)
    if max(get_distances(example_parsed)) == 1120:
        parsed = parse(puzzle.input_data)
        puzzle.answer_a = max(get_distances(parsed, 2503))

    if get_most_points(example_parsed) == 689:
        puzzle.answer_b = get_most_points(parsed, 2503)
