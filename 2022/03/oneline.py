# fmt: off
print(sum("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index((set(x[len(x)//2:])&set(x[:len(x)//2])).pop()) for x in open('2022/03/input').readlines()))
print(sum("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index((set(x)&set(y)&set(z)).pop()) for x,y,z in zip(*[iter(open('2022/03/input').read().split('\n'))]*3)))
