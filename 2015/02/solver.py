def wrapping(a, b, c):
    return 2 * (a * b + a * c + b * c) + min(a * b, a * c, b * c)


def ribbon(a, b, c):
    return 2 * (a + b + c - max(a, b, c)) + a * b * c


def solve(input_data):
    p1 = sum(wrapping(*map(int, line.split("x"))) for line in input_data.split("\n"))
    p2 = sum(ribbon(*map(int, line.split("x"))) for line in input_data.split("\n"))
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        p1, p2 = solve(input_data)
    print("Part 1:", p1)
    print("Part 2:", p2)
