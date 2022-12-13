from aocd.models import Puzzle


def equal(a, b):
    if type(a) == type(b) == int:
        return a == b
    if type(a) == int:
        a = [a]
    elif type(b) == int:
        b = [b]
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if not equal(a[i], b[i]):
            return False
    return True


def less_than(a, b):
    if equal(a, b):
        return True
    if type(a) == type(b) == int:
        return a < b
    if type(a) == int:
        a = [a]
    if type(b) == int:
        b = [b]
    for x in range(min(len(a), len(b))):
        if not equal(a[x], b[x]):
            return less_than(a[x], b[x])
    return len(a) < len(b)


puzzle = Puzzle(2022, 13)
input = [line.split("\n") for line in puzzle.input_data.strip().split("\n\n")]

total_list = [[[2]], [[6]]]
part1 = 0
for index, packet_pair in enumerate(input, 1):
    for packet in packet_pair:
        packet = eval(packet)
        for i in range(len(total_list)):
            if less_than(packet, total_list[i]):
                total_list.insert(i, packet)
                break
        else:
            total_list.append(packet)
    if less_than(eval(packet_pair[0]), eval(packet_pair[1])):
        part1 += index

puzzle.answer_a = part1
puzzle.answer_b = (total_list.index([[2]]) + 1) * (total_list.index([[6]]) + 1)
