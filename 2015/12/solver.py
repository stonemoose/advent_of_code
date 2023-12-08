from pydoc import doc
import re
import json

from aocd.models import Puzzle

puzzle = Puzzle(2015, 12)

puzzle.answer_a = sum([int(n) for n in re.findall("-?\d+", puzzle.input_data)])


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


puzzle.answkr_b = rec_sum(json.loads(puzzle.input_data))
