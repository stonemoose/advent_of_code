def map_next_category(category, maps):
    next_category = []
    for item in category:
        for min_max, increase in maps.items():
            if item >= min_max[0] and item <= min_max[1]:
                next_category.append(item + increase)
                break
        else:
            next_category.append(item)
    return next_category


def map_next_category_range(category, maps):
    next_category = []
    while category:
        start, end = category.pop(0)
        for min_max, increase in maps.items():
            if start >= min_max[0] and start <= min_max[1]:

                if end <= min_max[1]:
                    next_category.append([start + increase, end + increase])
                    break

                else:
                    next_category.append([start + increase, min_max[1] + increase])
                    category.append([min_max[1] + 1, end])
                    break

            elif end <= min_max[1] and end >= min_max[0]:
                next_category.append([min_max[0] + increase, end + increase])
                category.append([start, min_max[0] - 1])
                break
        else:
            next_category.append([start, end])
    return next_category


def solve(input_data):
    text = input_data.split("\n\n")

    seeds = [int(t) for t in text[0].split(":")[1].split()]
    range_seeds = [
        [seeds[i], sum(seeds[i : i + 2])] for i in range(0, len(seeds) // 2, 2)
    ]

    for line in text[1:]:
        maps = {}
        for mapping in line.split("\n")[1:]:
            mapping = [int(t) for t in mapping.split()]
            maps[(mapping[1], mapping[1] + mapping[2] - 1)] = mapping[0] - mapping[1]
        seeds = map_next_category(seeds, maps)
        range_seeds = map_next_category_range(range_seeds, maps)

    p1 = min(seeds)
    p2 = min(range_seeds)[0]
    return p1, p2


if __name__ == "__main__":
    with open("input") as f:
        p1, p2 = solve(f.read().strip)

    print("part 1: ", p1)
    print("part 2: ", p2)
