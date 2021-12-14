from collections import Counter


def next_step(formula_counter):
    new_formula = Counter()
    for p in formula_counter:
        if pairs[p]:
            new_formula[p[0]+pairs[p]] += formula_counter[p]
            new_formula[pairs[p] + p[1]] += formula_counter[p]
        else:
            new_formula[p] += formula_counter[p]
    return new_formula


def most_least_difference(formula_counter, formula):
    letter_counter = Counter()
    for key in formula_counter:
        letter_counter[key[0]] += formula_counter[key]
        letter_counter[key[1]] += formula_counter[key]
    for key in letter_counter:
        letter_counter[key] //= 2

    letter_counter[formula[0]] += 1
    letter_counter[formula[-1]] += 1
    most_common = letter_counter.most_common()
    return most_common[0][1] - most_common[-1][1]


if __name__ == '__main__':

    with open('input') as f:
        formula, pairs = f.read().strip().split('\n\n')
    pairs = dict([p.split(' -> ') for p in pairs.split('\n')])
    formula_counter = Counter(a+b for a, b in zip(formula[:-1], formula[1:]))

    for _ in range(10):
        formula_counter = next_step(formula_counter)
    print('Part 1: ', most_least_difference(formula_counter, formula))

    for _ in range(10, 40):
        formula_counter = next_step(formula_counter)
    print('Part 2: ', most_least_difference(formula_counter, formula))
