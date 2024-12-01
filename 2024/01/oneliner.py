from aocd.models import Puzzle
print(sum([abs(l-r) for l, r in zip(*map(sorted, zip(*[[int(n) for n in line.split()] for line in Puzzle(2024, 1).input_data.strip().split('\n')])))]))
print((lambda ls, rs: sum([l*rs.count(l) for l in ls]))(*zip(*[[int(n) for n in line.split()] for line in Puzzle(2024, 1).input_data.strip().split('\n')])))