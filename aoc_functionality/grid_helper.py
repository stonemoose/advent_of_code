def get_neighbours(x, y, max_x, max_y, min_x=0, min_y=0, all_dirs=False):
    if all_dirs:
        directions = [(-1, 0), (-1, 1), (0, 1), (1,1), (1, 0), (1,-1), (0, -1), (-1,-1)]
    else:
        # top, right, bottom, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dir_x, dir_y in directions:
        neighbour_x = x + dir_x 
        neighbour_y = y + dir_y 
        if min_x <= neighbour_x < max_x and min_y <= neighbour_y < max_y:
            yield neighbour_x, neighbour_y
    return

def print_grid(grid, boolean=False):
    for line in grid:
        for char in line:
            if boolean:
                if char:
                    print('#', end='')
                else:
                    print(' ', end='')
            else:
                print(char, end='')
        print()