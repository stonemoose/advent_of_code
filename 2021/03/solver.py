def find_common(bit_numbers, most_common):

    possible_numbers = set(bit_numbers)

    for i in range(len(bit_numbers[0])):
        ones = set(num for num in possible_numbers if num[i] == "1")
        zeros = possible_numbers - ones

        if (len(ones) >= len(zeros)) == most_common:
            possible_numbers = ones
        else:
            possible_numbers = zeros

        if len(possible_numbers) == 1:
            return int(possible_numbers.pop(), 2)


if __name__ == "__main__":

    with open("input") as f:
        bit_nums = [line.strip() for line in f.readlines()]

    gamma = [round(sum(map(int, n)) / len(bit_nums)) for n in zip(*bit_nums)]
    gamma = int("".join(map(str, gamma)), 2)
    epsilon = (1 << len(bit_nums[0])) - 1 - gamma

    print(f"Part 1: {gamma*epsilon}")

    o2 = find_common(bit_nums, True)
    co2 = find_common(bit_nums, False)

    print(f"Part 2: {co2*o2}")
