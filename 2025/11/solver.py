from aocd.models import Puzzle
from functools import cache


def parse(input_data):
    graph = {}
    for line in input_data.strip().split("\n"):
        node, *edges = line.split()
        graph[node[:-1]] = edges
    return graph


def solve(input_data):
    @cache
    def dfs_count(start, goal):
        if start == goal:
            return 1
        if start not in graph:
            return 0
        count = 0
        for other_node in graph[start]:
            if goal == "dac" and other_node == "fft":
                continue
            if goal == "fft" and other_node == "dac":
                continue
            count += dfs_count(other_node, goal)
        return count

    p1 = p2 = 0
    graph = parse(input_data)
    p1 = dfs_count("you", "out")

    fft_dac = dfs_count("fft", "dac")
    dac_fft = dfs_count("dac", "fft")
    if fft_dac:
        svr_fft = dfs_count("svr", "fft")
        dac_out = dfs_count("dac", "out")
        p2 = svr_fft * fft_dac * dac_out
    else:
        svr_dac = dfs_count("svr", "dac")
        fft_out = dfs_count("fft", "out")
        p2 = svr_dac * dac_fft * fft_out

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 11)
    p1, p2 = solve(puzzle.input_data)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
