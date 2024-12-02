with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


matching = dict(["()", "[]", "{}", "<>"])
corrupt_points = {")": 3, "]": 57, "}": 1197, ">": 25137}

illegal_chars = []
incomplete_points = []
for line in lines:
    opened = []
    for char in line:
        if char in "([{<":
            opened.append(char)
        else:
            if char != matching[opened.pop()]:
                illegal_chars.append(char)
                break
    else:
        line_out = 0
        for char in opened[::-1]:
            line_out *= 5
            line_out += "0([{<".index(char)
        incomplete_points.append(line_out)

incomplete_points.sort()
print("Part 1:", sum([corrupt_points[char] for char in illegal_chars]))
print("Part 2:", incomplete_points[len(incomplete_points) // 2])
