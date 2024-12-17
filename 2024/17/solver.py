import re
from aocd.models import Puzzle


def parse(input_data):
    register_str, program_str = input_data.split("\n\n")
    registers = {}
    for line in register_str.split("\n"):
        reg, num = line.split(": ")
        reg = reg.split()[1]
        registers[reg] = int(num)

    program = [int(n) for n in re.findall(r"\d+", program_str)]

    return registers, program


def combo(operand, a, b, c):
    match operand:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7:
            raise Exception("Invalid program")
        case _:
            return operand


def run_program(registers, program):
    a = registers["A"]
    b = registers["B"]
    c = registers["C"]
    out = []
    ip = 0

    while ip < len(program) - 1:
        opcode = program[ip]
        operand = program[ip + 1]

        match opcode:
            case 0:
                a = a >> combo(operand, a, b, c)
            case 1:
                b = b ^ operand
            case 2:
                b = combo(operand, a, b, c) % 8
            case 3:
                if a:
                    ip = operand
                    continue
            case 4:
                b = b ^ c
            case 5:
                out.append(combo(operand, a, b, c) % 8)
            case 6:
                b = a >> combo(operand, a, b, c)
            case 7:
                c = a >> combo(operand, a, b, c)

        ip += 2
    return out


def get_solution(registers, program, current=0):
    for i in range(8):
        next_curr = current + i
        registers["A"] = next_curr
        output = run_program(registers, program)
        if program == output:
            return next_curr
        if program[-len(output) :] == output:
            if solution := get_solution(registers, program, next_curr * 8):
                return solution
    return False


def solve(input_data):
    registers, program = parse(input_data)
    p1 = ",".join(str(n) for n in run_program(registers, program))
    p2 = get_solution(registers, program)
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2024, 17)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
