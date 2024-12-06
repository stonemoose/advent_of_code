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


def print_grid(grid, boolean=False):
    for line in grid:
        for char in line:
            if boolean:
                if char:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                print(char, end="")
        print()
