from collections import defaultdict

score_1 = score_2 = 0
pos1 = 2 - 1
pos2 = 7 - 1
die = 0


for total_rolls in range(3, 1000000, 3):
    roll = 0
    for _ in range(3):
        die = die % 100 + 1
        roll += die

    if total_rolls % 2:
        pos1 = (pos1 + roll) % 10
        score_1 += pos1 + 1
        if score_1 >= 1000:
            print(f"Part 1: {score_2*total_rolls}")
            break
    else:
        pos2 = (pos2 + roll) % 10
        score_2 += pos2 + 1
        if score_2 >= 1000:
            print(f"Part 1: {score_1*total_rolls}")
            break


def games_won(pos1, pos2):
    dice_rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    wins = [0, 0]
    universes = {(pos1, pos2, 0, 0): 1}

    while universes:
        next_universes = defaultdict(int)
        for data, num_unis in universes.items():
            pos1, pos2, score1, score2 = data
            for roll, num_rolls1 in dice_rolls.items():
                next_pos1 = (pos1 + roll) % 10
                next_score1 = score1 + next_pos1 + 1
                if next_score1 >= 21:
                    wins[0] += num_unis * num_rolls1
                else:
                    for roll, num_rolls2 in dice_rolls.items():
                        next_pos2 = (pos2 + roll) % 10
                        next_score2 = score2 + next_pos2 + 1
                        if next_score2 >= 21:
                            wins[1] += num_unis * num_rolls1 * num_rolls2
                        else:
                            next_universes[
                                (next_pos1, next_pos2, next_score1, next_score2)
                            ] += (num_unis * num_rolls1 * num_rolls2)
        universes = next_universes
    return wins


pos1 = 2 - 1
pos2 = 7 - 1
player1, player2 = games_won(pos1, pos2)
if player1 > player2:
    print(f"Part 2: {player1}")
else:
    print(f"Part 2: {player2}")
