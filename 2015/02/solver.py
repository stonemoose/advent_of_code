
def wrapping(a, b, c):
    return 2*(a*b + a*c + b*c) + min(a*b, a*c, b*c)


def ribbon(a, b, c):
    return 2*(a + b + c - max(a, b, c)) + a*b*c


with open('input') as f:
    print(sum(wrapping(*map(int, line.split('x'))) for line in f.readlines()))
with open('input') as f:
    print(sum(ribbon(*map(int, line.split('x'))) for line in f.readlines()))
