from aocd.models import Puzzle
import numpy as np


def parse(input_data):
    return [list(line) for line in input_data.strip().split("\n")]


def solver(parsed, start=(-1, 0, "right")):
    energized = np.zeros_like(parsed, dtype=int)
    beams = [start]
    before = set()
    sum_possible = 0
    while beams:
        x, y, direction = beams.pop()
        if (x, y, direction) in before:
            continue
        before.add((x, y, direction))

        try:
            match direction:
                case "right":
                    x += 1
                    energized[y, x] = 1
                    while True:
                        match parsed[y][x]:
                            case "." | "-":
                                x += 1
                                energized[y, x] = 1
                            case "\\":
                                beams.append((x, y, "down"))
                                break
                            case "/":
                                beams.append((x, y, "up"))
                                break
                            case "|":
                                beams.append((x, y, "up"))
                                beams.append((x, y, "down"))
                                break
                case "left":
                    x -= 1
                    if x < 0:
                        raise Exception
                    energized[y, x] = 1
                    while True:
                        match parsed[y][x]:
                            case "." | "-":
                                x -= 1
                                if x < 0:
                                    raise Exception
                                energized[y, x] = 1
                            case "\\":
                                beams.append((x, y, "up"))
                                break
                            case "/":
                                beams.append((x, y, "down"))
                                break
                            case "|":
                                beams.append((x, y, "up"))
                                beams.append((x, y, "down"))
                                break
                case "up":
                    y -= 1
                    if y < 0:
                        raise Exception
                    energized[y, x] = 1
                    while True:
                        match parsed[y][x]:
                            case "." | "|":
                                y -= 1
                                if y < 0:
                                    raise Exception
                                energized[y, x] = 1
                            case "\\":
                                beams.append((x, y, "left"))
                                break
                            case "/":
                                beams.append((x, y, "right"))
                                break
                            case "-":
                                beams.append((x, y, "left"))
                                beams.append((x, y, "right"))
                                break
                case "down":
                    y += 1
                    energized[y, x] = 1
                    while True:
                        match parsed[y][x]:
                            case "." | "|":
                                y += 1
                                energized[y, x] = 1
                            case "\\":
                                beams.append((x, y, "right"))
                                break
                            case "/":
                                beams.append((x, y, "left"))
                                break
                            case "-":
                                beams.append((x, y, "left"))
                                beams.append((x, y, "right"))
                                break
        except:
            pass

    return sum(sum(energized))


def get_best_solve(parsed):
    best = 0
    for y in range(len(parsed)):
        best = max(best, solver(parsed, (-1, y, "right")))
        best = max(best, solver(parsed, (len(parsed[0]), y, "left")))
    for x in range(len(parsed[0])):
        best = max(best, solver(parsed, (x, -1, "down")))
        best = max(best, solver(parsed, (x, len(parsed), "up")))
    return best


def solve(input_data):
    parsed = parse(input_data)
    p1 = solver(parsed)
    p2 = get_best_solve(parsed)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2023, 16)

    parsed_ex = parse(puzzle.examples[0].input_data)
    assert solver(parsed_ex) == 46
    parsed = parse(puzzle.input_data)
    puzzle.answer_a = solver(parsed)
    assert get_best_solve(parsed_ex) == 51
    puzzle.answer_b = get_best_solve(parsed)
