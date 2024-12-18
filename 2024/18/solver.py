from aocd.models import Puzzle
import aoc_functionality.grid_helper as gh


def parse(input_data):
    out = []
    for line in input_data.split("\n"):
        n1, n2 = line.split(",")
        out.append((int(n1), int(n2)))

    return out


def shortest_path(falling_bytes, num_bytes=1024, size=71):
    corrupted = set(falling_bytes[:num_bytes])
    start = (0, 0)
    end = (size - 1, size - 1)
    queue = [(0, start)]
    visited = {start}

    while queue:
        score, current = queue.pop(0)
        for neighbour in gh.get_neighbours(current[0], current[1], size, size):
            if neighbour in visited or neighbour in corrupted:
                continue
            queue.append((score + 1, neighbour))
            visited.add(neighbour)
            if neighbour == end:
                return score + 1

    return False


def find_first_unreachable(falling_bytes, size=71):
    left = 0
    right = len(falling_bytes)
    while left <= right:
        middle = (left + right) // 2
        if shortest_path(falling_bytes, middle, size):
            left = middle + 1
        else:
            right = middle - 1
    return falling_bytes[middle - 1]


def solve(input_data, num_bytes=1024, size=71):
    falling_bytes = parse(input_data)
    p1 = shortest_path(falling_bytes, num_bytes, size)
    p2 = find_first_unreachable(falling_bytes, size)
    return p1, f"{p2[0]},{p2[1]}"


if __name__ == "__main__":
    puzzle = Puzzle(2024, 18)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
