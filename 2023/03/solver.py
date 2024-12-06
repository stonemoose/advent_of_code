import re


def diagonal_symbol(data, i, start, end):
    def has_symbol(text):
        return re.search(r"[^0-9\.]", text)

    if i > 0:
        if has_symbol(data[i - 1][start - (start > 0) : end + (end < len(data[i]))]):
            return True

    if start > 0:
        if has_symbol(data[i][start - 1]):
            return True

    if end < (len(data[i]) - 1):
        if has_symbol(data[i][end]):
            return True

    if i < (len(data) - 1):
        if has_symbol(data[i + 1][start - (start > 0) : end + (end < len(data[i]))]):
            return True
    return False


def gear_ratio(data, i, start, end):
    ans = 0
    if i > 0:
        for match in re.finditer(r"\d+", data[i - 1]):
            if set(range(match.start(), match.end() + 1)) & set(range(start, end + 1)):
                if not ans:
                    ans = int(match[0])
                else:
                    return ans * int(match[0])

    for match in re.finditer(r"\d+", data[i]):
        if set(range(match.start(), match.end() + 1)) & set(range(start, end + 1)):
            if not ans:
                ans = int(match[0])
            else:
                return ans * int(match[0])

    if i < len(data) - 1:
        for match in re.finditer(r"\d+", data[i + 1]):
            if set(range(match.start(), match.end() + 1)) & set(range(start, end + 1)):
                if not ans:
                    ans = int(match[0])
                else:
                    return ans * int(match[0])


def solve(input_data):
    data = input_data.split("\n")

    ans1 = ans2 = 0

    for i, line in enumerate(data):
        for match in re.finditer(r"\d+", line):
            if diagonal_symbol(data, i, match.start(), match.end()):
                ans1 += int(match[0])
        for match in re.finditer(r"\*", line):
            gr = gear_ratio(data, i, match.start(), match.end())
            if gr:
                ans2 += gr

    return ans1, ans2


if __name__ == "__main__":
    with open("input") as f:
        ans1, ans2 = solve(f.read().strip())

    print("Part 1:", ans1)
    print("Part 2:", ans2)
