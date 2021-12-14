from collections import Counter


def next_step(formula_counter, pair_rules):
    new_formula = Counter()
    for key in formula_counter:
        try:
            new_formula[key[0] + pair_rules[key]] += formula_counter[key]
            new_formula[pair_rules[key] + key[1]] += formula_counter[key]
        except KeyError:
            new_formula[key] += formula_counter[key]
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
    pair_rules = dict([p.split(' -> ') for p in pairs.split('\n')])
    formula_counter = Counter(a+b for a, b in zip(formula[:-1], formula[1:]))

    for _ in range(10):
        formula_counter = next_step(formula_counter, pair_rules)
    print('Part 1: ', most_least_difference(formula_counter, formula))

    for _ in range(10, 40):
        formula_counter = next_step(formula_counter, pair_rules)
    print('Part 2: ', most_least_difference(formula_counter, formula))
