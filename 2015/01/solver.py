with open('input') as f:
    input = f.readline().strip()
    print(f'part 1: {input.count("(") - input.count(")")}')
    level = 0
    for pos, char in enumerate(input, 1):
        level += int(char == '(')
        if level < pos/2:
            print(f'part 2: {pos}')
            break
