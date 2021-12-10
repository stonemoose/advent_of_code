
with open('input') as f:
    lines = [line.strip() for line in f.readlines()]


matching = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

corrupted = 0
total_out = []
for line in lines:
    line_out = 0
    opened = []
    for char in line:
        if char in '([{<':
            opened.append(char)
            continue
        elif not opened:
            break
        elif char == ')' and opened.pop() != '(':
            corrupted += 3
            opened = None
            break
        elif char == ']' and opened.pop() != '[':
            corrupted += 57
            opened = None
            break
        elif char == '}' and opened.pop() != '{':
            corrupted += 1197
            opened = None
            break
        elif char == '>' and opened.pop() != '<':
            corrupted += 25137
            opened = None
            break
    if opened:
        for char in opened[::-1]:
            line_out *= 5
            line_out += '0([{<'.index(char)
        total_out.append(line_out)

total_out.sort()
print(corrupted)
print(total_out[len(total_out)//2])
