def solve(input_data):
    p1 = input_data.count("(") - input_data.count(")")
    level = 0
    for pos, char in enumerate(input_data, 1):
        level += int(char == "(")
        if level < pos / 2:
            p2 = pos
            break
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        input_data = f.readline().strip()
        p1, p2 = solver(input_data)
        print(f"part 1: {p1}")
        print(f"part 2: {p2}")
