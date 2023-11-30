from aocd.models import Puzzle
import re


def column(grid, x):
    return "".join([row[x] for row in grid if x < len(row) and row[x] != " "])


log = False
log2 = True
log = log2 = True


def move_right(board, x, y, steps):
    if steps == 0:
        return x, y
    if log:
        print(f"moving right from {x} {y}")
    try:
        if board[x][y + 1] == "#":
            return x, y
        if board[x][y + 1] == ".":
            return move_right(board, x, y + 1, steps - 1)
    except IndexError:
        pass

    wrapped_y = (re.search("\.|#", board[x])).start()
    if log2:
        print(f"wrap right: {x}, {y} -> {x}, {wrapped_y}")
    if board[x][wrapped_y] == "#":
        if log2:
            print("Crash")
        return x, y
    else:
        return move_right(board, x, wrapped_y, steps - 1)


def move_left(board, x, y, steps):
    if steps == 0:
        return x, y
    if log:
        print(f"moving left from {x} {y}")
    if board[x][y - 1] == "#":
        return x, y
    if board[x][y - 1] == ".":
        return move_left(board, x, (y - 1) % (len(board[x]) + 1), steps - 1)

    wrapped_y = len(board[x]) - 1 - re.search("\.|#", board[x][::-1]).start()
    if log2:
        print(f"wrap left: {x}, {y} -> {x}, {wrapped_y}")
    if board[x][wrapped_y] == "#":
        if log2:
            print("-" * 50 + "Crash")
        return x, y
    else:
        return move_left(board, x, wrapped_y, steps - 1)


def move_down(board, x, y, steps):
    if steps == 0:
        return x, y
    if log:
        print(f"moving down from {x} {y}")
    try:
        if board[x + 1][y] == "#":
            return x, y
        if board[x + 1][y] == ".":
            return move_down(board, x + 1, y, steps - 1)
    except IndexError:
        pass

    wrapped_x = x - (re.search("\.|#", column(board, y))).start()
    if log2:
        print(f"wrap down: {x}, {y} -> {wrapped_x}, {y}")
    if board[wrapped_x][y] == "#":
        if log2:
            print("Crash")
        return x, y
    else:
        return move_down(board, wrapped_x, y, steps - 1)


def move_up(board, x, y, steps):
    if steps == 0:
        return x, y
    if log:
        print(f"moving up from {x} {y}")
    try:
        if board[x - 1][y] == "#":
            return x, y
        if board[x - 1][y] == ".":
            return move_up(board, (x - 1) % (len(column(board, y)) + 1), y, steps - 1)
    except IndexError:
        pass

    column_y = column(board, y)
    wrapped_x = x + len(column_y) - 1 - re.search("\.|#", column_y[::-1]).start()
    if log2:
        print(f"wrap up: {x}, {y} -> {wrapped_x}, {y}")
        print(f"{column_y[::-1]}")
    if board[wrapped_x][y] == "#":
        if log2:
            print("Crash")
        return x, y
    else:
        return move_up(board, wrapped_x, y, steps - 1)


puzzle = Puzzle(2022, 22)

input_data = puzzle.input_data.strip("\n").split("\n\n")
pos = (0, 50)
# input_data = puzzle.example_data.strip("\n").split("\n\n")
# pos = (0, 8)
board = input_data[0].split("\n")
moves = re.findall("\d+|\D", input_data[1])


# right: '>': 0,
# down:  'v': 1,
# left:  '<': 2,
# up:    '^': 3,
dir = 0

if log:
    for row in board:
        print(row)

# moves += ["L", "L", "10", "R", "11", "L", "3", "R", "3"]
if log:
    print(pos, dir)
for move in moves:
    if move == "L":
        if log:
            print("turn left")
        dir = (dir - 1) % 4
    elif move == "R":
        if log:
            print("turn right")
        dir = (dir + 1) % 4
    else:
        if log:
            print("steps:", move)
        if dir == 0:
            pos = move_right(board, *pos, int(move))
        elif dir == 1:
            pos = move_down(board, *pos, int(move))
        elif dir == 2:
            pos = move_left(board, *pos, int(move))
        elif dir == 3:
            pos = move_up(board, *pos, int(move))

ans = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dir
print(ans)
puzzle.answer_a = ans
