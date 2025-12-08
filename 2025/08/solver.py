from aocd.models import Puzzle
import math


def parse(input_data):
    parsed = []
    for line in input_data.strip().split():
        parsed.append(tuple(int(n) for n in line.split(",")))
    return parsed


def find_edges(points):
    edges = []
    for i, point in enumerate(points, 1):
        for other_point in points[i:]:
            edges.append((point, other_point))
    edges.sort(key=lambda edge: math.dist(*edge))
    return edges


def min_span_tree(edges):
    graphs = []
    last_connection = None

    for start, end in edges:
        for graph in graphs:
            if start in graph:
                start_graph = graph
                break
        else:
            start_graph = {start}
            graphs.append(start_graph)

        if end in start_graph:
            continue

        for graph in graphs:
            if end in graph:
                graphs.remove(graph)
                start_graph.update(graph)
                break
        else:
            start_graph.add(end)

        last_connection = (start, end)

    return sorted([len(g) for g in graphs], reverse=True), last_connection


def solve(input_data, connections=1000):
    p1 = p2 = 0
    parsed = parse(input_data)
    edges = find_edges(parsed)

    first_1000 = min_span_tree(edges[:connections])[0]
    p1 = math.prod(first_1000[:3])

    last_connection = min_span_tree(edges)[1]
    p2 = last_connection[0][0] * last_connection[1][0]

    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2025, 8)
    p1, p2 = solve(puzzle.input_data)

    if p1:
        puzzle.answer_a = p1
    if p2:
        puzzle.answer_b = p2
