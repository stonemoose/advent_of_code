import re
from copy import deepcopy


with open("2022/05/input") as f:
    stack_info, proc_info = [p.split("\n") for p in f.read().strip().split("\n\n")]

stacks = [[] for _ in range(10)]
for line in stack_info[:-1]:
    for crate in re.finditer(r"[A-Z]", line):
        stacks[int(stack_info[-1][crate.start()])].append(crate.group())

stacks2 = deepcopy(stacks)
procedure = [map(int, re.findall(r"\d+", line)) for line in proc_info]

for amount, from_stack, to_stack in procedure:
    for _ in range(amount):
        stacks[to_stack].insert(0, stacks[from_stack].pop(0))

    stacks2[to_stack] = stacks2[from_stack][:amount] + stacks2[to_stack]
    stacks2[from_stack] = stacks2[from_stack][amount:]

print("Part 1:", "".join(stack[0] for stack in stacks[1:]))
print("Part 2:", "".join(stack[0] for stack in stacks2[1:]))
