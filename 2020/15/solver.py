def spoken_number(numbers, n=2020):
    numbers = numbers.copy()
    prev = 0
    for i in range(len(numbers), n - 1):
        spoken = i - numbers[prev] if prev in numbers else 0
        numbers[prev] = i
        prev = spoken
    return prev


def solve(input_data):
    numbers = {int(n): i for i, n in enumerate(input_data.split(","))}

    return spoken_number(numbers, 2020), spoken_number(numbers, 30_000_000)


if __name__ == "__main__":
    with open("input") as f:
        numbers = {int(n): i for i, n in enumerate(f.read().strip().split(","))}

    print(numbers)
    prev = 0
    for i in range(len(numbers), 29999999):
        spoken = i - numbers[prev] if prev in numbers else 0
        numbers[prev] = i
        prev = spoken
    print(prev)
