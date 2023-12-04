# fmt: off
[print(sum(x)) for x in zip(*[((ord(y)-ord(o)-1)%3*3+ord(y)-87,(ord(y)-88)*3+(ord(y)+ord(o)-1)%3+1) for o, y in [l.split() for l in open("2022/02/input").readlines()]])]
