from copy import deepcopy
import numpy as np
import re
from aoc_functionality.util import print_progress_bar

from aocd.models import Puzzle


class Monkey:
    def __init__(self, str_rep, mod_num):
        self.items = list(map(int, re.findall("\d+", str_rep[1])))
        self.operation = lambda old: eval(str_rep[2].split(" = ")[1]) % mod_num
        num, true_monkey, false_monkey = list(map(int, re.findall("\d+", str_rep[3])))
        self.test = lambda x: true_monkey if x % num == 0 else false_monkey
        self.inspect_counter = 0

    def inspect(self):
        self.items = list(map(self.operation, self.items))
        self.inspect_counter += len(self.items)


def solve(monkey_list, rounds, divisor=1):
    monkey_list = deepcopy(monkey_list)
    for i in range(rounds):
        print_progress_bar(i, rounds - 1)
        for monkey in monkey_list:
            monkey.inspect()
            while monkey.items:
                item = monkey.items.pop() // divisor
                monkey_list[monkey.test(item)].items.append(item)
    return np.prod(sorted([m.inspect_counter for m in monkey_list])[-2:])


puzzle = Puzzle(2022, 11)

mod = np.prod(list(map(int, re.findall("divisible by (\d+)", puzzle.input_data))))
monkey_list = [Monkey(m.split("\n", 3), mod) for m in puzzle.input_data.split("\n\n")]
puzzle.answer_a = solve(monkey_list, 20, 3)
puzzle.answer_b = solve(monkey_list, 10000)
