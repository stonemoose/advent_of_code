# fmt: off
print(sum([len(set(l.replace('\n', ''))) for l in open('input').read().strip().split('\n\n')]))
print(sum([len(set.intersection(*map(set, l.split('\n')))) for l in open('input').read().strip().split('\n\n')]))
