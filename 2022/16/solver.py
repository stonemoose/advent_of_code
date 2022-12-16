from aocd.models import Puzzle
from aoc_functionality.util import print_progress_bar

BIG_NUM = 100


def setup(valve_info):
    valve_info.sort(key=lambda x: x[0])
    name_to_index = {valve[0]: index for index, valve in enumerate(valve_info)}
    num_valves = len(valve_info)
    neighbour_matrix = [[BIG_NUM] * num_valves for _ in range(num_valves)]
    flow_rates = [0] * num_valves
    for i, valve in enumerate(valve_info):
        flow_rates[i] = valve[1]
        for neighbour in valve[2]:
            neighbour_matrix[i][name_to_index[neighbour]] = 1
    return neighbour_matrix, flow_rates


def full_neighbour_matrix(neighbour_matrix, flow_rates):
    changed = True
    num_neighbours = len(neighbour_matrix)

    while changed:
        changed = False
        for i in range(num_neighbours):
            for k in range(num_neighbours):
                if neighbour_matrix[i][k]:
                    for n in range(num_neighbours):
                        if (
                            neighbour_matrix[i][n]
                            > neighbour_matrix[i][k] + neighbour_matrix[k][n]
                        ):
                            neighbour_matrix[i][n] = (
                                neighbour_matrix[i][k] + neighbour_matrix[k][n]
                            )
                            changed = True

    for i, rate in enumerate(flow_rates[1:], 1):
        if rate == 0:
            for k in range(num_neighbours):
                neighbour_matrix[k][i] = 0
            neighbour_matrix[i] = [0] * num_neighbours

    return neighbour_matrix


# def get_matrix_without_zero!


def solve(input):
    valve_info = []
    for line in input:
        _, name, _, _, rate, _, _, _, _, *lead_to = line.split()
        valve_info.append([name, int(rate.split("=")[1][:-1]), list(lead_to)])

    neighbour_matrix, flow_rates = setup(valve_info)
    neighbour_matrix = full_neighbour_matrix(neighbour_matrix, flow_rates)

    def get_pressure(opened=(0,), current=0, current_flow_rate=0, pressure=0, time=30):
        pressure += current_flow_rate
        current_flow_rate += flow_rates[current]

        unopened = [
            i for i in range(len(flow_rates)) if i not in opened and flow_rates[i]
        ]
        time_walked = sum(
            neighbour_matrix[opened[i - 1]][opened[i]] for i in range(1, len(opened))
        )
        time_left = time - time_walked - len(opened) + 1

        possible_values = []
        for valve in unopened:
            if neighbour_matrix[current][valve] < time_left:
                possible_values.extend(
                    get_pressure(
                        opened + (valve,),
                        valve,
                        current_flow_rate,
                        pressure + current_flow_rate * neighbour_matrix[current][valve],
                        time=time,
                    )
                )
        # stay
        possible_values.append((pressure + current_flow_rate * time_left, opened))
        return possible_values

    pressures = get_pressure()
    print("part 1:", max(pressures)[0])
    pressures = sorted(get_pressure(time=26), reverse=True)

    best = 0

    current = pressures[0]
    for other in pressures[1:]:
        if current[0] + other[0] > best and set(current[1]) & set(other[1]) == {0}:
            best = current[0] + other[0]
            break
    for i in range(len(pressures)):
        print_progress_bar(i, len(pressures) - 1)
        current = pressures[i]
        for other in pressures[i + 1 :]:
            if current[0] + other[0] > best and set(current[1]) & set(other[1]) == {0}:
                best = current[0] + other[0]
                break
            elif current[0] + other[0] < best:
                break
    print("part 2:", best)


puzzle = Puzzle(2022, 16)
input = puzzle.input_data.strip().replace(",", "").split("\n")


solve(input)
