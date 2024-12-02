# fmt: off
import numpy as np


# part 1
print(sum([l[y*3 % len(l)] == '#' for y, l in enumerate(open('input').read().splitlines())]))
# part 2
print(np.prod([sum([l[y*r % len(l)] == '#' for y, l in enumerate(open('input').read().splitlines()[::d])]) for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))
