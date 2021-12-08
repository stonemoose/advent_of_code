with open('input') as f:
    lines = [line.strip().split(' | ') for line in f.readlines()]


ans = 0
final_ans2 = 0
for pattern, output in lines:
    segments = {
        'top_left': '',
        'bot_left': '',
        'top': '',
        'mid': '',
        'bot': '',
        'top_right': '',
        'bot_right': '',
    }
    patterns = pattern.split(' ')
    zero = None
    one = None
    two = None
    three = None
    four = None
    five = None
    six = None
    seven = None
    eight = None
    nine = None
    for p in list(patterns):
        if len(p) == 2:
            one = p
            patterns.remove(p)
        if len(p) == 3:
            seven = p
            patterns.remove(p)
        if len(p) == 4:
            four = p
            patterns.remove(p)
        if len(p) == 7:
            eight = p
            patterns.remove(p)
    for p in patterns:
        if len(set(p).intersection(four)) == 4:
            nine = p
        elif len(p) == 6:
            if len(set(p).intersection(one)) == 2:
                zero = p
            else:
                six = p
        elif len(set(p).intersection(one)) == 2:
            three = p
        elif len(set(p).intersection(four)) == 3:
            five = p
        else:
            two = p
    ans2 = 0
    for num in output.split(' '):
        ans2 *= 10
        if len(num) in (2, 3, 4, 7):
            ans += 1
        if set(num) == set(zero):
            pass
        elif set(num) == set(one):
            ans2 += 1
        elif set(num) == set(two):
            ans2 += 2
        elif set(num) == set(three):
            ans2 += 3
        elif set(num) == set(four):
            ans2 += 4
        elif set(num) == set(five):
            ans2 += 5
        elif set(num) == set(six):
            ans2 += 6
        elif set(num) == set(seven):
            ans2 += 7
        elif set(num) == set(eight):
            ans2 += 8
        elif set(num) == set(nine):
            ans2 += 9
    final_ans2 += ans2
    print(ans2)
print(ans)
print(final_ans2)
