from aocd.models import Puzzle
from aoc_functionality.util import print_progress_bar
import math


class Module:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.inputs = {}

    def recieve_pulse(self, sender, high: bool):
        raise NotImplementedError


class FlipFlop(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.state = False

    def recieve_pulse(self, sender, high: bool):
        if high:
            return []
        self.state = not self.state
        for module in self.destinations:
            yield (module, self.name, self.state)


class Conjunction(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)

    def recieve_pulse(self, sender, high: bool):
        self.inputs[sender] = high
        sending = not all(self.inputs.values())
        for module in self.destinations:
            yield (module, self.name, sending)


class Broadcast(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)

    def recieve_pulse(self, sender, high: bool):
        for module in self.destinations:
            yield (module, self.name, high)


class OutPut(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)

    def recieve_pulse(self, sender, high: bool):
        return []


class Button(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.pressed = 0

    def press(self):
        self.pressed += 1
        return (self.destinations[0], self.name, False)


def parse(input_data):
    return [line.split(" -> ") for line in input_data.strip().split("\n")]


def setup(parsed):
    modules = {"button": Button("button", ["broadcaster"])}
    for name, destinations in parsed:
        destinations = destinations.split(", ")
        match name[0]:
            case "%":
                modules[name[1:]] = FlipFlop(name[1:], destinations)
            case "&":
                modules[name[1:]] = Conjunction(name[1:], destinations)
            case "b":
                modules["broadcaster"] = Broadcast("broadcaster", destinations)
    for mod in modules:
        for other_mod in modules[mod].destinations:
            if other_mod in modules:
                modules[other_mod].inputs[mod] = False
    return modules


def solve(input_data):
    parsed = parse(input_data)
    modules = setup(parsed)
    cycles = {mod: None for mod in modules["vf"].inputs}
    low_pulses = 0
    high_pulses = 0
    for presses in range(1000):
        pulses = [("broadcaster", "button", False)]
        while pulses:
            reciever, sender, high = pulses.pop(0)
            high_pulses += high
            low_pulses += not high
            if reciever not in modules:
                continue
            for new_pulse in modules[reciever].recieve_pulse(sender, high):
                pulses.append(new_pulse)
            if reciever in cycles:
                if not any(modules[reciever].inputs.values()):
                    cycles[reciever].append(presses)

    while not all(cycles.values()):
        presses += 1
        pulses = [("broadcaster", "button", False)]
        while pulses:
            reciever, sender, high = pulses.pop(0)
            if reciever not in modules:
                continue
            for new_pulse in modules[reciever].recieve_pulse(sender, high):
                pulses.append(new_pulse)
            if reciever in cycles:
                if not any(modules[reciever].inputs.values()):
                    cycles[reciever] = presses + 1

    button_presses = math.prod(cycles.values())
    return low_pulses * high_pulses, button_presses


if __name__ == "__main__":
    puzzle = Puzzle(2023, 20)
    puzzle.answer_a, puzzle.answer_b = solve(puzzle.input_data)
