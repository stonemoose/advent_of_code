from aocd.models import Puzzle


def parse(input_data):
    data = []
    counter = 0
    space = False
    for num in input_data:
        if space:
            data.append((int(num), None))
        else:
            data.append((int(num), counter))
            counter += 1
        space = not space

    return data


def helper(line):
    while True:
        amount, num = line.pop()
        if num is None:
            continue
        while amount:
            for i, space_new_num in enumerate(line):
                space, new_num = space_new_num
                if new_num is None:
                    if amount >= space:
                        line[i] = (space, num)
                        amount -= space
                    elif amount < space:
                        line[i] = (space - amount, None)
                        line.insert(i, (amount, num))
                        amount = 0
                        break
            else:
                line.append((amount, num))
                return line


def helper2(line):
    counter = 0
    while abs(counter) < len(line):
        counter -= 1
        amount, num = line[counter]
        if num is None:
            continue
        for i, space_new_num in enumerate(line[:counter]):
            space, new_num = space_new_num
            if new_num is None:
                if amount == space:
                    line[counter] = (amount, None)
                    line[i] = (space, num)
                    break
                if amount < space:
                    line[counter] = (amount, None)
                    line[i] = (space - amount, None)
                    line.insert(i, (amount, num))
                    break
    return line


def solve(input_data):
    parsed = parse(input_data)
    p1 = p2 = 0

    count = 0
    for amount, num in helper(parsed.copy()):
        for _ in range(amount):
            p1 += (count) * int(num)
            count += 1

    count = 0
    for amount, num in helper2(parsed):
        for _ in range(amount):
            if num is not None:
                p2 += (count) * int(num)
            count += 1

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 9)

    ex1, ex2 = solve(puzzle.examples[0].input_data)
    p1, p2 = solve(puzzle.input_data)

    assert ex1 == 1928
    puzzle.answer_a = p1
    assert ex2 == 2858
    puzzle.answer_b = p2
