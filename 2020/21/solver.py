from collections import defaultdict

ingredient_dict = defaultdict(list)
ingredient_list = []
with open('input') as f:
    for line in f.read().strip().split('\n'):
        ingredients, allergens = line[:-1].split(' (')
        allergens = allergens[9:].split(', ')
        ingredients = set(ingredients.split(' '))
        for allergen in allergens:
            ingredient_dict[allergen].append(ingredients)
        ingredient_list.append(ingredients)

allergen_set = set()
# allergen_tuples = []
for allergen, ingredients in ingredient_dict.items():
    possible_ingredients = set.intersection(*ingredients)
    allergen_set.update(possible_ingredients)
    print(allergen, end=': ')
    print(possible_ingredients)
    # allergen_tuples.append([allergen, possible_ingredients])


print('Part 1:', sum(len(ing - allergen_set) for ing in ingredient_list))
#  Part 2: xgtj,ztdctgq,bdnrnx,cdvjp,jdggtft,mdbq,rmd,lgllb
