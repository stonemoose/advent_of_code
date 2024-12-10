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
    for _ in range(loop_size):
        value *= subject_number
        value = value % DIVIDER
    return value


def solve(input_data):
    card_public, door_public = [int(n) for n in input_data.split("\n")]
    p1 = encrypt(card_public, find_loopsize(7, door_public))
    return p1, 0
