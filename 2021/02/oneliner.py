# fmt: off
print((lambda l: l[0]*l[1])([sum(i) for i in zip(*map(lambda t: (int(t[1])*(t[0][0]=='f'),int(t[1])*(t[0][0]=='d')-int(t[1])*(t[0][0]=='u')),[l.strip().split() for l in open('input').readlines()]))]))
