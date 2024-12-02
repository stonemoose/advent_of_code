# fmt: off
from itertools import combinations
from math import prod

[print(f'{len(x)}: {prod(x)}') for x in (filter(lambda x: sum(x) == 2020, (c for l in [2, 3] for c in combinations((int(n) for n in open('input').readlines()), l))))]
