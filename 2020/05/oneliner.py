# Part 1
print(max([int(''.join(map(lambda x: '10'['B' < x < 'R'], l)), 2) for l in open('input').read().splitlines()]))
# Part 2
(lambda x: print(set(range(x[0], x[-1])).difference(x).pop()))(sorted([int(''.join(map(lambda x: '10'['B' < x < 'R'], l)), 2) for l in open('input').read().splitlines()]))
