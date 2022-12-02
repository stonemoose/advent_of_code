with open("2022/02/input") as f:
    rounds = [l for l in f.read().strip().split("\n")]

full_rules = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
full_rules2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

print("Part 1:", sum([full_rules[round] for round in rounds]))
print("Part 2:", sum([full_rules2[round] for round in rounds]))
