from aoc_functionality.util import print_progress_bar

from aocd.models import Puzzle


class Brick:
    i = 0

    def __init__(self, coords: set):
        self.name = Brick.i
        Brick.i += 1
        self.coords = coords
        self.supports: list[Brick] = []
        self.supported_by = []

    def remove_brick(self, fallen):
        fallen.add(self)
        for other_brick in self.supports:
            if len(set(other_brick.supported_by) - fallen) < 1:
                fallen.update(other_brick.remove_brick(fallen))

        return fallen

    def __lt__(self, other):
        return min([c[2] for c in self.coords]) < min([c[2] for c in other.coords])

    def __hash__(self):
        return id(self)


def make_brick(start, end):
    start = [int(n) for n in start.split(",")]
    end = [int(n) for n in end.split(",")]
    brick_coords = set()
    for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
        for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            for z in range(min(start[2], end[2]), max(start[2], end[2]) + 1):
                brick_coords.add((x, y, z))

    return Brick(brick_coords)


def parse(input_data):
    return [make_brick(*line.split("~")) for line in input_data.strip().split("\n")]


def fall(bricks: list[Brick]):
    structure: list[Brick] = []
    for i, brick in enumerate(bricks):
        print_progress_bar(i, len(bricks) - 1)
        new_coords = set()
        falling = True
        while falling:
            if min([coord[2] for coord in brick.coords]) == 1:
                brick.supported_by.append("Ground")
                break
            new_coords = {(coord[0], coord[1], coord[2] - 1) for coord in brick.coords}

            for other_brick in structure:
                if new_coords.intersection(other_brick.coords):
                    brick.supported_by.append(other_brick)
                    other_brick.supports.append(brick)
                    falling = False
            if falling:
                brick.coords = new_coords
        structure.append(brick)

    desintegratable = 0
    desintegrate_consequence = 0
    for brick in bricks:
        would_fall = len(brick.remove_brick(set())) - 1
        desintegrate_consequence += would_fall
        desintegratable += not would_fall

    return desintegratable, desintegrate_consequence


def solve(bricks):
    return fall(sorted(bricks))


if __name__ == "__main__":
    puzzle = Puzzle(2023, 22)
    example = parse(puzzle.example_data)
    assert solve(example) == (5, 7)

    parsed = parse(puzzle.input_data)
    puzzle.answer_a, puzzle.answer_b = solve(parsed)
