# fmt: off
print(list(map(sum, (zip(*[[[a:=a.replace(n[1:], n[1:] + n) for n in ("1one 2two 3three 4four 5five 6six 7seven 8eight 9nine".split())], int((b:=[c for c in l if c.isdigit()])[0] + b[-1]), int((b:=[c for c in a if c.isdigit()])[0] + b[-1])][1:] for l in open("input") if (a:=l)])))))
