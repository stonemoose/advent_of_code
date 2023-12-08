from aocd.models import Puzzle

puzzle = Puzzle(2015, 8)

def parse(input_data):
    return input_data.strip().split('\n')
    
def solve(input_data):
    full = len(''.join(input_data))
    represented = len(''.join([eval(l) for l in input_data]))
    escaped = len(''.join([repr(l).replace('\"', '\\"') for l in input_data]))
    return full-represented, escaped-full

puzzle.answer_a, puzzle.answer_b = solve(parse(puzzle.input_data))