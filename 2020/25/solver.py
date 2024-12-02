DIVIDER = 20201227


def find_loopsize(subject_number, public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value *= subject_number
        value = value % DIVIDER
        loop_size += 1
    return loop_size


def encrypt(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value = value % DIVIDER
    return value


with open("input") as f:
    card_public, door_public = [int(n) for n in f.read().strip().split("\n")]


print(find_loopsize(7, card_public))
print(find_loopsize(7, door_public))
print(encrypt(card_public, find_loopsize(7, door_public)))
print(encrypt(door_public, find_loopsize(7, card_public)))
