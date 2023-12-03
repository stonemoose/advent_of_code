import math


def parse_games(line):
    game_id, game_text = line.strip().split(": ")
    game_id = int(game_id[5:])
    game = [round.split(", ") for round in game_text.split("; ")]
    return game_id, game


with open("input") as f:
    data = f.read().strip().split("\n")


part1 = part2 = 0

for line in data:
    g_id, game = parse_games(line)
    max_dict = {"green": 0, "red": 0, "blue": 0}

    for round in game:
        for value_color in round:
            value, color = value_color.split()
            max_dict[color] = max(max_dict[color], int(value))

    part2 += math.prod(max_dict.values())
    if max_dict["green"] <= 13 and max_dict["red"] <= 12 and max_dict["blue"] <= 14:
        part1 += g_id


print("Part 1:", part1)
print("Part 2:", part2)
