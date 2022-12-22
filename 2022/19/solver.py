from aocd.models import Puzzle
from functools import cache
from multiprocessing import Pool
import re
import numpy as np


class BluePrint:
    def __init__(self, id, ore, clay, obs_ore, obs_clay, geode_ore, geode_obs):
        self.id = id
        self.ore = ore
        self.clay = clay
        self.obsidian = (obs_ore, obs_clay)
        self.geode = (geode_ore, geode_obs)

        self.max_ore = max(ore, clay, obs_ore, geode_ore)
        self.max_clay = obs_clay
        self.max_obs = geode_obs

    def __str__(self):
        return f"{self.id} A:{self.ore} B:{self.clay} C:{self.obsidian} D:{self.geode}"

    def __has__(self):
        return hash((self.id, self.ore, self.clay, self.obsidian, self.geode))

    def build_ore(self, supply, robots):
        new_supply = (
            supply[0] - self.ore,
            supply[1],
            supply[2],
            supply[3],
        )
        new_robots = (
            robots[0] + 1,
            robots[1],
            robots[2],
            robots[3],
        )
        return new_supply, new_robots

    def build_clay(self, supply, robots):
        new_supply = (
            supply[0] - self.clay,
            supply[1],
            supply[2],
            supply[3],
        )
        new_robots = (
            robots[0],
            robots[1] + 1,
            robots[2],
            robots[3],
        )
        return new_supply, new_robots

    def build_obs(self, supply, robots):
        new_supply = (
            supply[0] - self.obsidian[0],
            supply[1] - self.obsidian[1],
            supply[2],
            supply[3],
        )
        new_robots = (
            robots[0],
            robots[1],
            robots[2] + 1,
            robots[3],
        )
        return new_supply, new_robots

    def build_geode(self, supply, robots):
        new_supply = (
            supply[0] - self.geode[0],
            supply[1],
            supply[2] - self.geode[1],
            supply[3],
        )
        new_robots = (
            robots[0],
            robots[1],
            robots[2],
            robots[3] + 1,
        )
        return new_supply, new_robots


def parse_input(input):
    blueprints = []
    for line in input:
        blueprints.append(BluePrint(*map(int, re.findall("\d+", line))))
    return blueprints


def part_2(bp: BluePrint):
    return max_geodes(bp, time_left=32)[0] // bp.id


@cache
def max_geodes(
    bp: BluePrint,
    supply=(0, 0, 0, 0),
    robots=(1, 0, 0, 0),
    time_left=24,
):
    # supply/robots = (ore, clay, obsidian, geode)
    if time_left <= 1:
        return (supply[3] + robots[3]) * bp.id, supply, robots

    new_supply = tuple(supply[i] + robots[i] for i in range(4))

    if supply[0] >= bp.geode[0] and supply[2] >= bp.geode[1]:
        geode_supply, geode_robots = bp.build_geode(new_supply, robots)
        return max_geodes(bp, geode_supply, geode_robots, time_left - 1)

    possible = []
    if (
        supply[0] >= bp.obsidian[0]
        and supply[1] >= bp.obsidian[1]
        and robots[2] < bp.max_obs
    ):
        obs_supply, obs_robots = bp.build_obs(new_supply, robots)
        possible.append(max_geodes(bp, obs_supply, obs_robots, time_left - 1))

    if supply[0] >= bp.ore and robots[0] < bp.max_ore:
        ore_supply, ore_robots = bp.build_ore(new_supply, robots)
        possible.append(max_geodes(bp, ore_supply, ore_robots, time_left - 1))

    if supply[0] >= bp.clay and robots[1] < bp.max_clay:
        clay_supply, clay_robots = bp.build_clay(new_supply, robots)
        possible.append(max_geodes(bp, clay_supply, clay_robots, time_left - 1))

    # don't do nothing if too much resources
    if supply[0] > 2 * bp.max_ore or supply[2] > 1.5 * bp.max_obs:
        possible.append((0, new_supply, robots))
    else:
        possible.append(max_geodes(bp, new_supply, robots, time_left - 1))

    return max(possible)


puzzle = Puzzle(2022, 19)
input = puzzle.input_data.strip().split("\n")
blueprints = parse_input(input)

with Pool(len(blueprints)) as p:
    puzzle.answer_a = sum(m[0] for m in p.map(max_geodes, blueprints))

with Pool(3) as p:
    puzzle.answer_b = np.prod(list(p.map(part_2, blueprints[:3])))
