# fmt: off
import re
from aocd.models import Puzzle
    
print(sum((int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", Puzzle(2024, 3).input_data))))
print(sum((int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", re.sub(r"don't\(\)(?s:(?!do\(\)).)*", "", Puzzle(2024, 3).input_data)))))

