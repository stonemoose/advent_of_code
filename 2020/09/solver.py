with open('input') as f:
    numbers = [int(n) for n in f.read().strip().split('\n')]


def sum_of_earlier(num, earlier):
    return set(earlier).intersection(set(num-n for n in earlier))


invalid = 0
for i, num in enumerate(numbers[25:]):
    if not sum_of_earlier(num, numbers[i: i+25]):
        invalid = num
        print(num)
        break

for i in range(len(numbers)):
    sum_nums = numbers[i]
    for j in range(i+1, len(numbers)):
        sum_nums += numbers[j]
        if sum_nums > invalid:
            break
        elif sum_nums == invalid:
            print(max(numbers[i:j+1]) + min(numbers[i:j+1]))
            quit()
