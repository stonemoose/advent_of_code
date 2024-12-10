from aocd.models import Puzzle


def parse(input_data):
    start_time, buses = input_data.split("\n")
    buses = enumerate(buses.split(","))
    buses = [(i % int(bus), int(bus)) for i, bus in buses if not bus == "x"]
    start_time = int(start_time)
    return start_time, buses


def solve(input_data):
    start_time, buses = parse(input_data)
    t_delta = t = buses[0][1]

    for i, bus in buses[1:]:
        while bus - (t % bus) != i:
            t += t_delta
        t_delta *= bus

    first = min(buses, key=lambda x: x[1] - start_time % x[1])[1]
    p1 = first * (first - (start_time % first))
    p2 = t
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 13)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
