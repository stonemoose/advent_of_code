from collections import Counter


def key_func(hand_val):
    card_order = "23456789TJQKA"
    hand = sorted(Counter(hand_val[0]).values(), reverse=True)
    return hand, tuple(card_order.index(c) for c in hand_val[0])


def key_func2(hand_val):
    card_order = "J23456789TQKA"
    hand = Counter(hand_val[0])
    jokers = 0
    if "J" in hand and len(hand) > 1:
        jokers = hand.pop("J")
    hand = sorted(hand.values(), reverse=True)
    hand[0] += jokers
    return hand, tuple(card_order.index(c) for c in hand_val[0])


def solve(input_data):
    text = [l.split() for l in input_data.split("\n")]

    text.sort(key=key_func)
    part1 = sum([int(hand_value[1]) * rank for rank, hand_value in enumerate(text, 1)])

    text.sort(key=key_func2)
    part2 = sum([int(hand_value[1]) * rank for rank, hand_value in enumerate(text, 1)])

    return part1, part2


if __name__ == "__main__":
    with open("input") as f:
        part1, part2 = solve(f.read().strip())

    print("Part 1: ", part1)
    print("Part 2: ", part2)
