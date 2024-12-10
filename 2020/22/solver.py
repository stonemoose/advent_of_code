from copy import deepcopy


def play(deck1, deck2):
    deck1, deck2 = deepcopy(deck1), deepcopy(deck2)
    while deck1 and deck2:
        top1, top2 = deck1.pop(0), deck2.pop(0)
        if top1 > top2:
            deck1.append(top1)
            deck1.append(top2)
        elif top2 > top1:
            deck2.append(top2)
            deck2.append(top1)
    return deck1 or deck2


def recursive_play(deck1, deck2):
    already_played = []
    deck1, deck2 = deepcopy(deck1), deepcopy(deck2)
    while deck1 and deck2:
        if (deck1, deck2) in already_played:
            deck1.append(deck1.pop(0))
            deck1.append(deck2.pop(0))
            return deck1, True
        else:
            already_played.append((deepcopy(deck1), deepcopy(deck2)))

        top1, top2 = deck1.pop(0), deck2.pop(0)
        if top1 <= len(deck1) and top2 <= len(deck2):
            if recursive_play(deck1[:top1], deck2[:top2])[1]:
                deck1.append(top1)
                deck1.append(top2)
            else:
                deck2.append(top2)
                deck2.append(top1)

        elif top1 > top2:
            deck1.append(top1)
            deck1.append(top2)
        elif top2 > top1:
            deck2.append(top2)
            deck2.append(top1)
    if deck1:
        return deck1, True
    if deck2:
        return deck2, False


def score(deck):
    return sum(i * card for i, card in enumerate(deck[::-1], 1))


def solve(input_data):
    deck1, deck2 = [d.split("\n")[1:] for d in input_data.split("\n\n")]
    deck1 = [int(card) for card in deck1]
    deck2 = [int(card) for card in deck2]

    p1 = score(play(deck1, deck2))
    p2 = score(recursive_play(deck1, deck2)[0])
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        p1, p2 = solve(f.read().strip())
    print("Part 1:", p1)
    print("Part 2:", p2)
