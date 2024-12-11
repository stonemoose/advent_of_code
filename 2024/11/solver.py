from aocd.models import Puzzle
from collections import defaultdict
from functools import cache


def parse(input_data):
    stones = defaultdict(int)
    for num in input_data.split(" "):
        stones[int(num)] += 1
    return stones


def blink_once(stones):
    new_stones = defaultdict(int)
    for stone, num in stones.items():
        if stone == 0:
            new_stones[1] += num
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            middle = len(str_stone) // 2
            new_stones[int(str_stone[:middle])] += num
            new_stones[int(str_stone[middle:])] += num
        else:
            new_stones[stone * 2024] += num
    return new_stones


@cache
def blink_recursive(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return blink_recursive(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        middle = len(str_stone) // 2
        return blink_recursive(int(str_stone[:middle]), blinks - 1) + blink_recursive(
            int(str_stone[middle:]), blinks - 1
        )
    else:
        return blink_recursive(stone * 2024, blinks - 1)


def solve_recursive(input_data):
    stones = parse(input_data)
    p1 = p2 = 0

    p1 = sum(blink_recursive(stone, 25) for stone in stones)
    p2 = sum(blink_recursive(stone, 75) for stone in stones)
    return p1, p2


def solve(input_data):
    stones = parse(input_data)
    p1 = p2 = 0

    for _ in range(25):
        stones = blink_once(stones)
    p1 = sum(stones.values())
    for _ in range(50):
        stones = blink_once(stones)
    p2 = sum(stones.values())
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 11)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
