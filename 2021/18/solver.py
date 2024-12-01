import copy
import math
from itertools import permutations

from aoc_functionality.util import print_progress_bar

def flatten(main_list, depth=0):
    for el in main_list:
        if isinstance(el, list):
            for sub_el in flatten(el, depth+1):
                yield sub_el
        else:
            yield {'value': el, 'depth': depth}


def check_explode(list_num):
    for i, element in enumerate(list_num):
        if element['depth'] == 4:
            second_el = i+1

            if i > 0:
                list_num[i-1]['value'] += element['value']
            if second_el < len(list_num) - 1:
                list_num[second_el+1]['value'] += list_num[second_el]['value']

            del list_num[i]
            list_num[i]['value'] = 0
            list_num[i]['depth'] = 3

            break


def check_split(list_num):
    for i, num in enumerate(list_num):
        if num['value'] >= 10:
            list_num[i] = {
                'value': math.floor(num['value']/2),
                'depth': num['depth']+1
            }
            list_num.insert(i+1, {
                'value': math.ceil(num['value']/2),
                'depth': num['depth']+1
            })
            break


def reduce_snail(flat_number):

    next_flat_number = []
    while next_flat_number != flat_number:
        next_flat_number = copy.deepcopy(flat_number)
        check_explode(flat_number)
        if next_flat_number == flat_number:
            check_split(flat_number)
    return flat_number


def pprint(flat_number):
    print(' '.join(str(fn['value']) + '-' + str(fn['depth']) for fn in flat_number))




def magnitude(flat_numbers):
    while len(flat_numbers) > 1:
        for i in range(0, len(flat_numbers), 1):
            try:
                if flat_numbers[i]['depth'] == flat_numbers[i+1]['depth']:
                    flat_numbers[i] = {
                        'value': flat_numbers[i]['value']*3 + flat_numbers[i+1]['value']*2,
                        'depth': flat_numbers[i]['depth']-1
                    }
                    del flat_numbers[i+1]
                    break
            except Exception:
                print(i)
                pprint(flat_numbers)
                quit()
    return flat_numbers[0]['value']


def find_best_mag(all_lines):
    best_mag = 0
    line_num = 0
    max_l = len(list(permutations(all_lines, 2)))
    for lines in permutations(all_lines, 2):
        print_progress_bar(line_num, max_l-1)
        line_num += 1
        new_line = copy.deepcopy(lines[0]) + copy.deepcopy(lines[1])
        for num in new_line:
            num['depth'] += 1
        new_line = reduce_snail(new_line)

        best_mag = max(best_mag, magnitude(new_line))
    return best_mag


with open('2021/18/input') as f:
    lines = [list(flatten((eval(line.strip())))) for line in f.readlines()]
    part2_lines = copy.deepcopy(lines)

while len(lines) > 1:
    new_line = lines[0] + lines[1]
    for num in new_line:
        num['depth'] += 1
    new_line = reduce_snail(new_line)
    del lines[0]
    lines[0] = new_line

print(f'part 1: {magnitude(new_line)}')
print(f'part 2: {find_best_mag(part2_lines)}')
