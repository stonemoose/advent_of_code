def solve(length, signal):
    for i in range(length, len(signal)):
        if len(signal[i - length : i]) == len(set(signal[i - length : i])):
            return i


with open("2022/06/input") as f:
    sig = f.readline()

print(f"Part 1: {solve(4, sig)}")
print(f"Part 2: {solve(14, sig)}")
