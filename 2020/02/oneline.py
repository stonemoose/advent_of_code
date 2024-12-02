# fmt: off
import re

print(sum(map(lambda x: int(x[0]) <= x[3].count(x[2]) <= int(x[1]), (re.split(r'-| |: ', l) for l in open('input').readlines()))))

print(sum(map(lambda x: (x[3][int(x[0])-1] == x[2]) ^ (x[3][int(x[1])-1] == x[2]), (re.split(r'-| |: ', l) for l in open('input').readlines()))))
