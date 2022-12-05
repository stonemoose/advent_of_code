# fmt: off
print(sum(__import__('string').ascii_letters.index((set(x[len(x)//2:])&set(x[:len(x)//2])).pop())+1 for x in open('2022/03/input').readlines()))
print(sum(__import__('string').ascii_letters.index((set(x)&set(y)&set(z)).pop())+1 for x,y,z in zip(*[iter(open('2022/03/input').read().split('\n'))]*3)))
