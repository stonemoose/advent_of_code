# fmt: off
print(sum((lambda a,b,c,d:(a<=c)&(b>=d)|(a>=c)&(b<=d))(*list(map(int,l.strip().replace("-",",").split(",")))) for l in open("input")))
print(sum((lambda a,b,c,d:max(a,c)<=min(b,d))(*list(map(int,l.strip().replace("-",",").split(",")))) for l in open("input")))
