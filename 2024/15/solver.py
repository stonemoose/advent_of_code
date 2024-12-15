from aocd.models import Puzzle
import aoc_functionality.grid_helper as gh
import copy


def parse(input_data):
    out = []
    maze, moves = input_data.split("\n\n")
    for line in maze.split("\n"):
        out.append(list(line))

    return out, "".join(moves.split("\n"))


def parse2(input_data):
    out = []
    maze, moves = input_data.split("\n\n")
    for line in maze.split("\n"):
        line_list = []
        for char in line:
            match char:
                case "#":
                    line_list.append("#")
                    line_list.append("#")
                case "O":
                    line_list.append("[")
                    line_list.append("]")
                case ".":
                    line_list.append(".")
                    line_list.append(".")
                case "@":
                    line_list.append("@")
                    line_list.append(".")
        out.append(line_list)
    return out, "".join(moves.split("\n"))


def push(pos, direction, grid):
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if grid[next_pos[0]][next_pos[1]] == ".":
        grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = "."
        return True
    elif grid[next_pos[0]][next_pos[1]] == "#":
        return False
    elif grid[next_pos[0]][next_pos[1]] == "O":
        if push(next_pos, direction, grid):
            grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = "."
            return True
        return False
    elif grid[next_pos[0]][next_pos[1]] == "[":
        if direction[0] == 0:
            second_pos = (next_pos[0] + direction[0], next_pos[1] + direction[1])
            if push(second_pos, direction, grid):
                grid[second_pos[0]][second_pos[1]] = grid[next_pos[0]][next_pos[1]]
                grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = "."
                return True

            return False
        else:
            second_pos = (next_pos[0], next_pos[1] + 1)
            if push(second_pos, direction, grid) and push(next_pos, direction, grid):
                grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = "."
                return True
            return False
    elif grid[next_pos[0]][next_pos[1]] == "]":
        if direction[0] == 0:
            second_pos = (next_pos[0] + direction[0], next_pos[1] + direction[1])
            if push(second_pos, direction, grid):
                grid[second_pos[0]][second_pos[1]] = grid[next_pos[0]][next_pos[1]]
                grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = "."
                return True
            return False
        else:
            second_pos = (next_pos[0], next_pos[1] - 1)
            if push(second_pos, direction, grid) and push(next_pos, direction, grid):
                grid[next_pos[0]][next_pos[1]] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = "."
                return True
            return False
    raise Exception("How did we get here")


def helper(warehouse, moves):
    pos = None
    for i, line in enumerate(warehouse):
        for j, char in enumerate(line):
            if char == "@":
                pos = (i, j)

    directions = {
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
        "^": (-1, 0),
    }
    for move in moves:
        old_grid = copy.deepcopy(warehouse)
        if push(pos, directions[move], warehouse):
            pos = (pos[0] + directions[move][0], pos[1] + directions[move][1])
        else:
            warehouse = old_grid

    gps_sum = 0
    for i, line in enumerate(warehouse):
        for j, char in enumerate(line):
            if char in "O[":
                gps_sum += 100 * i + j
    return gps_sum


def solve(input_data):
    warehouse, moves = parse(input_data)
    second_warehouse, _ = parse2(input_data)
    p1 = helper(warehouse, moves)
    p2 = helper(second_warehouse, moves)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 15)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
