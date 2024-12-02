from itertools import product, chain


def possible_locations(mask, mem):
    chars = [["0", "1"] if c == "X" else [c] for c in mask]
    mem_str = f"{mem:036b}"
    for i in range(len(mem_str)):
        if mem_str[i] == "1" and mask[i] == "0":
            chars[i] = ["1"]
    all_masks = chars[0]
    for char in chars[1:]:
        all_masks = [list(chain(prod[0], prod[1])) for prod in product(all_masks, char)]
    all_masks = [int("".join(mask), 2) for mask in all_masks]
    return all_masks


with open("input") as f:
    docking_data = [line.split(" = ") for line in f.read().strip().split("\n")]
memory1 = {}
memory2 = {}

for first, second in docking_data:
    if first == "mask":
        mask = second
    else:
        string = ""
        for digit, m_digit in zip(f"{int(second):036b}", mask):
            if m_digit == "X":
                string += digit
            else:
                string += m_digit
        memory1[first] = int(string, 2)

        mem = int(first[4:-1])
        for loc in possible_locations(mask, mem):
            memory2[loc] = int(second)


print(f"Part 1: {sum(memory1.values())}")
print(f"Part 2: {sum(memory2.values())}")
