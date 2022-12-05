# fmt: off
print(sum((lambda a,b,c,d:(a<=c)&(b>=d)|(a>=c)&(b<=d))(*(map(int,l.strip().replace("-",",").split(",")))) for l in open("input")))
print(sum((lambda a,b,c,d:(a<=d)&(c<=b))(*(map(int,l.strip().replace("-",",").split(",")))) for l in open("input")))
