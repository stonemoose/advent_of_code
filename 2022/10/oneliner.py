# fmt: off
print("\n".join(["".join(["█"if i%40-2<sum([int(s)if s.strip('-').isdigit() else 0 for s in open('i').read().replace('\n',' ').split()*2][:i])+1<i%40+2 else " " for i in range(240)][i*40:(i+1)*40])for i in range(6)]))
