def to_postfix(line):
    stack = []
    output = []
    for char in line:
        if char == "*":
            if stack and not stack[-1] == "(":
                output.append(stack.pop())
            stack.append(char)
        elif char == "+":
            if stack and not stack[-1] == "(":
                output.append(stack.pop())
            stack.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack:
                char = stack.pop()
                if char == "(":
                    break
                output.append(char)
        else:
            output.append(int(char))
    while stack:
        output.append(stack.pop())
    return output


def to_postfix_2(line):
    stack = []
    output = []
    for char in line:
        if char == "*":
            if stack and not stack[-1] == "(":
                output.append(stack.pop())
            stack.append(char)
        elif char == "+":
            if stack and stack[-1] == "+":
                output.append(stack.pop())
            stack.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack:
                char = stack.pop()
                if char == "(":
                    break
                output.append(char)
        else:
            output.append(int(char))
    while stack:
        output.append(stack.pop())
    return output


def postfix_solve(postfix_list):
    stack = []
    for char in postfix_list:
        if char == "*":
            stack.append(stack.pop() * stack.pop())
        elif char == "+":
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(char)
    return stack[0]


def solve(input_data):
    homework = input_data.split("\n")

    p1 = sum(postfix_solve(to_postfix(line.replace(" ", ""))) for line in homework)
    p2 = sum(postfix_solve(to_postfix_2(line.replace(" ", ""))) for line in homework)
    return p1, p2
