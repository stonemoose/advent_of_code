from pydoc import doc
import re
import json

from aocd.models import Puzzle


def rec_sum(document):
    in_object = type(document) == dict
    if in_object:
        document = document.values()
    ans = 0
    for inner_doc in document:
        match inner_doc:
            case int():
                ans += inner_doc
            case list():
                ans += rec_sum(inner_doc)
            case dict():
                ans += rec_sum(inner_doc)
            case "red":
                if in_object:
                    ans = 0
                    break
            case _:
                pass
    return ans


def solve(input_data):
    p1 = sum([int(n) for n in re.findall(r"-?\d+", input_data)])
    p2 = rec_sum(json.loads(input_data))
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2015, 12)
    puzzle.answer_a = sum([int(n) for n in re.findall(r"-?\d+", puzzle.input_data)])
    puzzle.answkr_b = rec_sum(json.loads(puzzle.input_data))
