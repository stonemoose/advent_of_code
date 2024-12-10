from aocd.models import Puzzle


def find_allergens(ingredient_dict):
    actual_ingredients = {}
    while ingredient_dict:
        for allergen, possible_ingredient in ingredient_dict.items():
            if len(possible_ingredient) == 1:
                del ingredient_dict[allergen]
                for other_allergens in ingredient_dict:
                    ingredient_dict[other_allergens] -= possible_ingredient
                actual_ingredients[allergen] = possible_ingredient.pop()
                break
    return actual_ingredients


def solve(input_data):
    ingredient_dict = {}
    ingredient_list = []
    for line in input_data.split("\n"):
        ingredients, allergens = line[:-1].split(" (")
        allergens = allergens[9:].split(", ")
        ingredients = set(ingredients.split(" "))
        for allergen in allergens:
            if allergen in ingredient_dict:
                ingredient_dict[allergen] &= ingredients
            else:
                ingredient_dict[allergen] = ingredients.copy()
        ingredient_list.append(ingredients)

    allergen_set = set.union(*ingredient_dict.values())
    p1 = sum(len(ing - allergen_set) for ing in ingredient_list)

    actual_ingredients = find_allergens(ingredient_dict)
    p2 = ",".join(ingredient for _, ingredient in sorted(actual_ingredients.items()))
    return p1, p2


if __name__ == "__main__":
    puzzle = Puzzle(2020, 21)
    p1, p2 = solve(puzzle.input_data)
    puzzle.answer_a = p1
    puzzle.answer_b = p2
