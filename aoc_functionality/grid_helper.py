import aoc_functionality.util as au

DIRECTIONS_STRAIGHT = ((-1, 0), (0, 1), (1, 0), (0, -1))
DIRECTIONS_DIAGONAL = ((-1, -1), (-1, 1), (1, 1), (1, -1))

DIRECTIONS_ALL = DIRECTIONS_STRAIGHT + DIRECTIONS_DIAGONAL


def get_neighbours(x, y, max_x, max_y, min_x=0, min_y=0, straight=True, diagonal=False):
    if not (straight or diagonal):
        raise Exception("No direction given")
    directions = []
    if diagonal:
        directions += DIRECTIONS_DIAGONAL
    if straight:
        directions += DIRECTIONS_STRAIGHT
    for dir_x, dir_y in directions:
        neighbour_x = x + dir_x
        neighbour_y = y + dir_y
        if min_x <= neighbour_x < max_x and min_y <= neighbour_y < max_y:
            yield neighbour_x, neighbour_y
    return


def coords_in_grid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid)


def print_grid(grid, bool_func=None, highlight_coords=None, second_highlight=None):
    string = ""
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if bool_func:
                char = "#" if bool_func(char) else "."
            if highlight_coords and (i, j) in highlight_coords:
                string += au.Color.PURPLE + str(char) + au.Color.END
            elif second_highlight and (i, j) in second_highlight:
                string += au.Color.CYAN + str(char) + au.Color.END
            else:
                string += str(char)
        string += "\n"
    print(string)
