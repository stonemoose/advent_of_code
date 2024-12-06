import hashlib


def solve(input_data):
    p1 = p2 = 0
    for i in range(10000000):
        result = hashlib.md5(f"{input_data.strip()}{i}".encode())
        if not p1 and result.hexdigest()[:5] == "00000":
            p1 = i
        if not p2 and result.hexdigest()[:6] == "000000":
            p2 = i
        if p1 and p2:
            break
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        p1, p2 = solve(f.read())

    print("Part 1:", p1)
    print("Part 2:", p2)
