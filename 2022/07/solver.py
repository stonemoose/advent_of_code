from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=7)
input = puzzle.input_data.split("\n")

system = {}
current_dir = []
for line in input:
    match line.strip().split():
        case "$", "cd", "..":
            current_dir.pop()
        case "$", "cd", dir_name:
            current_dir.append(dir_name)
            system["/".join(current_dir)] = 0
        case size, _ if size.isdigit():
            m = "/"
            system[m] += int(size)
            for x in current_dir[1:]:
                m += "/" + x
                system[m] += int(size)

puzzle.answer_a = sum(size for size in system.values() if size <= 100000)
free_space = 70000000 - system["/"]
puzzle.answer_b = min(size for size in system.values() if size + free_space >= 30000000)
