import re
from aocd.models import Puzzle
    
print(sum((int(n1) * int(n2) for n1, n2 in re.findall(r"mul\((\d+),(\d+)\)", Puzzle(2024, 3).input_data))))
