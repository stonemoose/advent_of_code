from aocd.models import Puzzle
import math
import re


def parse(input_data):
    return [line.split("\n") for line in input_data.strip().split("\n\n")]


def all_possible(workflow_dict):
    possible_values = {rating: (1, 4000) for rating in "xmas"}
    check_flows = [("in", possible_values)]
    accepted_parts = []
    while check_flows:
        flow, values = check_flows.pop()
        rules = workflow_dict[flow]
        for rule in rules[:-1]:
            rating, cond, number, next_flow = re.search(
                r"([xmas])([<>])([0-9]+):(.+)", rule
            ).groups()
            number = int(number)
            pass_values = values.copy()

            if cond == ">":
                pass_values[rating] = (number + 1, values[rating][1])
                values[rating] = (values[rating][0], number)
            elif cond == "<":
                pass_values[rating] = (values[rating][0], number - 1)
                values[rating] = (number, values[rating][1])

            match next_flow:
                case "A":
                    accepted_parts.append(pass_values)
                case "R":
                    continue
                case _:
                    check_flows.append((next_flow, pass_values))

        match rules[-1]:
            case "A":
                accepted_parts.append(values)
            case "R":
                continue
            case next_flow:
                check_flows.append((next_flow, values))

    number_accepted = sum(
        math.prod(map(lambda min_max: min_max[1] - min_max[0] + 1, part.values()))
        for part in accepted_parts
    )
    return number_accepted


def next_workflow(rules, x, m, a, s):
    for rule in rules[:-1]:
        condition, next_flow = rule.split(":")
        # xmas magic here
        if eval(condition):
            return next_flow
    return rules[-1]


def check_part(part, workflow_dict):
    workflow = "in"
    while workflow not in ("A", "R"):
        workflow = next_workflow(workflow_dict[workflow], **part)
    return workflow == "A"


def solve(input_data):
    parsed = parse(input_data)
    workflows, parts = parsed
    total_val = 0
    workflow_dict = {}
    for flow in workflows:
        name, rules = re.search(r"([a-z]+){(.*)}", flow).groups()
        workflow_dict[name] = rules.split(",")

    for part_str in parts:
        part = {}
        for rating_number in part_str[1:-1].split(","):
            rating, number = rating_number.split("=")
            part[rating] = int(number)

        if check_part(part, workflow_dict):
            total_val += sum(part.values())

    return total_val, all_possible(workflow_dict)


if __name__ == "__main__":
    puzzle = Puzzle(2023, 19)
    assert solve(puzzle.examples[0].input_data) == (19114, 167409079868000)
    puzzle.answer_a, puzzle.answer_b = solve(puzzle.input_data)
