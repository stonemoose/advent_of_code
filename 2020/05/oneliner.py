# Part 1
print(int(max(open('input').read().replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0').splitlines()), base=2))
# Part 2
(lambda x: print(next(iter(set(range(x[0], x[-1])).difference(x)))))(sorted([int(i, base=2) for i in open('input').read().replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0').splitlines()]))
