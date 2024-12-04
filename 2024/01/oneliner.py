# fmt: off
from aocd.models import Puzzle
print(sum([abs(l-r)for l,r in zip(*map(sorted,zip(*[map(int, l.split())for l in open('input').readlines()])))]))
print((lambda l,r: sum([s*r.count(s)for s in l]))(*zip(*[map(int, l.split())for l in open('input').readlines()])))
